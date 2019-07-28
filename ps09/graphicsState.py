# Code for showing state of a graphics object
#
# History: 
# [2017/09/18, lyn]
# * Modified valRep to apply round(v, 8) for all floating point numbers v. 
#   This helps to remove "scary" floats (notice by Eni) that come from transformations. 
#    E.g.,  6.123233995736766e-15 => 0.0
#           3.12499999999 => 3.25
#
# [2017/02/04-05, lyn] 
# * Added option (previously unsupported, default True) for printing Canvas components
# * Added option (previously supported, default True) for printing Layer components
# * Correctly accumulate context transforms of containers to show correct
#   global points, widhts, heights, radiuses, etc. for all transformed objects
# * Note that in general angle cannot be displayed because it's nonsensical in 
#   the presence of flips. My getAngle hack is cs1graphics.py helpful in simple animations, 
#   but is not helpful here. 
# [2017/01/31, lyn] Fixed points in Polygon and Path so that they are 
#  properly transformed
# [2017/01/29, lyn]
# * Display colors as lowercase strings. Tt turns out cs1graphics 
#   will lowercase and remove spaces from any color name, 
#   so you can use ' CY  AN   ' as a color!  Internally it uses
#   both some capitalized names (like 'Black', 'Transparent').
# * Added support for Images and Layers
# [2017/01/28, lyn] Created. No support for Images or Layers

import cs1graphics # Need this to refer to _Transformation as cs1graphics.Transformation
from cs1graphics import * # Need this to refer to other class by unprefixed name. 
import math

'''Dictionary that maps each class to a function that gets the state for
   that class'''
stateGetters = {
    Canvas: lambda obj,tform: [('width', obj.getWidth()), # Top-level canvas width is not transformed
                               ('height', obj.getHeight()), # Top-level canvas height is not transformed
                               ('backgroundColor', 
                                colorToString(obj.getBackgroundColor())),
                               ('title', obj.getTitle()), 
                               ('contents', Contents(obj,tform)), 
                               ],                         
    Circle: lambda obj,tform: [('radius', getRadius(obj,tform))], 
    Drawable: lambda obj,tform: ([('referencePoint', getReferencePoint(obj,tform)), 
                                  ('depth', obj.getDepth())]),
    Ellipse: lambda obj,tform: [('width', getWidth(obj,tform)), 
                                ('height', getHeight(obj,tform))],
    FillableShape: lambda obj,tform: [('fillColor', colorToString(obj.getFillColor()))],
    Image: # Note: an Image does not "know" the filename from which it
           # was constructed, so no way to grab that information.        
        lambda obj,tform: [('width', getWidth(obj,tform)),
                           ('height', getHeight(obj,tform))], 
    Layer: lambda obj,tform: [('contents', Contents(obj,tform))], 
    Path: lambda obj,tform: [('points', getPathOrPolyPoints(obj,tform))],
    Polygon: lambda obj,tform: [('points', getPathOrPolyPoints(obj,tform))],
    Rectangle: lambda obj,tform: [('width', getWidth(obj,tform)),
                                  ('height', getHeight(obj,tform))], 
    Shape: lambda obj,tform: [('borderColor', colorToString(obj.getBorderColor())),
                              ('borderWidth', getBorderWidth(obj,tform))],
    Square: lambda obj,tform: [('size', getSize(obj,tform))],
    Text: lambda obj,tform: [('messages', obj.getMessage()),
                             ('fontSize', getFontSize(obj,tform)),
                             ('fontColor', colorToString(obj.getFontColor()))]
}

# Graphics classes in topological sort from leaves to root in class hiearachy.
# The leaf-to-root order is important for listing more specific state varibles
# first when displaying object state. 
graphicsClasses = [Square, Rectangle, Circle, Polygon, Ellipse, FillableShape, Path, 
                   Shape, Text, Image, Layer, Drawable, Canvas]

def getClasses(obj):
    '''Returns a list of all graphics classes of which this object is an 
       instance, from bottom up.'''
    allClasses = [cl for cl in graphicsClasses if isinstance(obj,cl)]
    if Polygon in allClasses:
        allClasses.remove(Path) # For some reason, Polygon is considered
                                # subclass of Path, and we don't want that
    return allClasses
        

def getStatePairs(obj, transform):
    return reduce(lambda x,y: x+y, 
                  [stateGetters[cl](obj,transform) for cl in getClasses(obj)], 
                  [])

globalPrintContents = True # Controls whether contents should be printed

def printState(obj, shouldPrintContents=True):
    global globalPrintContents
    globalPrintContents = shouldPrintContents
    print graphicsState(obj, cs1graphics._Transformation())

def graphicsState(obj, transform):
    statePairs = getStatePairs(obj, transform)
    if statePairs == []:
        return "<Not a graphics object!>"
    else: 
        return objString(obj, statePairs)

def objString(obj, statePairs):
    return "<{className}:\n  {state}>".format(
      className=getClassName(obj),
      state=',\n  '.join(['{n}={v}'.format(n=name,v=valRep(val))
                           for (name,val) in statePairs])
    )

def getClassName(obj): 
    return obj.__class__.__name__
    
def colorToString(colorObj):
    '''Convert colorObj to lowercased string without spaces.
       It turns out s1graphics will lowercase and remove spaces 
       from any color name, so you can use ' CY  AN   ' as a color.  
       Internally it uses some capitalized names 
       (like 'Black', 'Transparent').'''
    return str(colorObj).lower().replace(' ','')
    
def valRep(val):
    if isinstance(val,list):
        return [valRep(obj) for obj in val]
    elif isinstance(val,tuple):
        return tuple([valRep(obj) for obj in val])
    elif isinstance(val,float):
        return round(val, 8) # Helps to remove "scary" floats that come from transformations. 
                             # E.g.,  6.123233995736766e-15 => 0.0
                             #        3.12499999999 => 3.25
    else:
        return val

def getReferencePoint(drawable, tform):
    '''Return the reference point of a drawable object. 
       Careful: this must be transformed not only by transform of object,
       but also by transform tform of containers.'''
    return tform.image(drawable.getReferencePoint())

def getPathOrPolyPoints(pathOrPoly, tform):
    '''Return a list of (x,y) coords of *transformed* points in a Path or Polygon. 
       Careful: this must be transformed not only by transform of pathOrPoly,
       but also by transform tform of containers.'''
    polyTform = tform*pathOrPoly._transform
    return [(pt.getX(),pt.getY()) for pt in 
             [polyTform.image(pathOrPoly.getPoint(i)) for i in 
              range(pathOrPoly.getNumberOfPoints())]]

def getWidth(drawable, tform):
    '''Return the width of the drawable object. 
       The width returned by drawable.getWidth() already takes into account
       the local transformations of the drawable itself.
       But this result also needs to be transformed by the tform of containers.'''
    #print "***getWidth:"
    #print "class=", getClassName(drawable)
    #print "transform=", drawable._transform
    #print "drawable.getWidth()=", drawable.getWidth()
    #print "drawable._transform.image(...)", Point(drawable.getWidth(),0)
    #print "transformedDistance:", transformedDistance(tform, Point(drawable.getWidth(),0))
    return transformedDistance(tform, Point(drawable.getWidth(),0))

def getHeight(drawable, tform):
    '''Return the height of the drawable object. 
       The height returned by drawable.getHeight() already takes into account
       the local transformations of the drawable itself.
       But this result also needs to be transformed by the tform of containers.'''
    return transformedDistance(tform, Point(0, drawable.getHeight()))

def getSize(sq, tform):
    '''Return the size of Square sq.
       The width/height/size returned by sq.getWidth() and friends already takes into account
       the local transformations of the sq itself.
       But this result also needs to be transformed by the tform of containers.
       Warning: This won't make sense if sq has been tranformed into a 
       non-square rectangle by a skew transform.'''
    return getWidth(sq, tform) # Assume width and height are the same

def getRadius(circ, tform):
    '''Return the radius of circ.
       The radius returned by circ.getRadius() already takes into account
       the local transformations of the circ itself.
       But this result also needs to be transformed by the tform of containers.
       Warning: This won't make sense if circle has been tranformed into an ellipse
       by a skew transform.'''
    return transformedDistance(tform, Point(circ.getRadius(),0))

def getBorderWidth(shape, tform):
    '''Return the border width of the shape object. 
       The border width returned by shape.getBorderWidth() already takes into account
       the local transformations of the shape itself.
       But this result also needs to be transformed by the tform of containers.
       Warning: This won't make sense if shape has been tranformed 
       by a skew transform.'''
    return transformedDistance(tform, Point(shape.getBorderWidth(),0))

def getFontSize(text, tform):
    '''Return the font size of the text object. 
       The font size text.getFontSize() already takes into account
       the local transformations of the text itself.
       But this result also needs to be transformed by the tform of containers.
       Warning: This won't make sense if shape has been tranformed 
       by a skew transform.'''
    return transformedDistance(tform, Point(0,text.getFontSize()))

def transformedDistance(tform,pt):
    '''Return the distance between the transformed given point
       and the transformed origin'''
    return distance(tform.image(Point(0,0)), tform.image(pt))

def distance(pt1, pt2):
    '''Return the distance between two points'''
    return math.sqrt((pt2.getX() - pt1.getX())**2 + (pt2.getY() - pt1.getY())**2)
                            
class Contents():
    '''Instances of this class are a collection of graphics objects. 
       This class exists solely for its __repr__ method, which returns
       a string-like entity without the quotes.'''

    def __init__(self, container, transform):
        containerClass = getClassName(container)
        self.objects = container.getContents() # List of contained graphics objects
        self.cumulativeTransform = transform*container._transform\
                                   if containerClass == 'Layer'\
                                   else transform
            
    def __repr__(self): 
        # The following is a single string with two obj strings separated
        # by a line 30 tildes
        if globalPrintContents: 
            sep = '\n'+'~'*30+'\n'
            separatedContentsString =\
                sep + sep.join([graphicsState(o, self.cumulativeTransform) for o in self.objects])\
                + sep[:-1] # Remove final newline 
            indent = 4*' '
            indentedSeparatedContentLines =\
                [indent + line for line in separatedContentsString.split('\n')]
            return '\n'.join(indentedSeparatedContentLines)
        else: 
            return "... details of {n} contained objects not shown ...".format(n=len(self.objects))

def testAll():
    tank = Canvas(600, 300, 'cyan', 'Fish tank')
    circ = Circle(50, Point(200, 100))
    circ.setFillColor('yellow')
    rect = Rectangle(100, 200, Point(300, 400))
    rect.setBorderColor('red')
    rect.setBorderWidth(17)
    wedge = Polygon(Point(0,100), Point(0,0), Point(200,100))
    wedge2 = wedge.clone()
    wedge2.setFillColor('green')
    wedge2.moveTo(100,400)
    path = Path(Point(0,100), Point(100,100), Point(100,0))
    path2 = path.clone()
    path2.setBorderColor('blue')
    path2.moveTo(300,200)

    # Fish example from Lect 02
    fish = Layer()

    # yellow body of the fish
    body = Ellipse(100,50,Point(0,0))
    body.setFillColor('yellow')
    fish.add(body)

    # green tail of the fish
    tail = Polygon(Point(-50,0), Point(-75,25), Point(-75,-25))
    tail.setFillColor('green')
    fish.add(tail)

    # black eye of the fish
    eye = Circle(5,Point(25,-5))
    eye.setFillColor('black')
    fish.add(eye)

    fish.moveTo(200,100)

    tank.add(fish)

    fish2 = fish.clone()
    tank.add(fish2)
    fish2.moveTo(125,225)
    fish2.scale(2)
    fish2.flip(0)

    fish3 = fish.clone()
    tank.add(fish3)
    fish3.moveTo(400,150)
    fish3.flip(0)
    fish3.scale(1.5)
    fish3.rotate(30)

    pinterest = Canvas(800, 600, 'pink', 'Pinwheels')

    bowtie = Polygon(Point(0,0), Point(-200,-50), Point(-200,50), Point(0,0), Point(200,-50), Point(200,50))
    bowtie.setFillColor('red')
    pinwheel = Layer()
    pinwheel.add(bowtie)

    bowtie2 = bowtie.clone()
    bowtie2.setFillColor('blue')
    bowtie2.rotate(90)
    pinwheel.add(bowtie2)

    pinwheels = Layer()
    pinwheel.moveTo(200, 200)
    pinwheels.add(pinwheel)
    
    pinwheel2 = pinwheel.clone()
    pinwheel2.moveTo(500,100)
    pinwheel2.scale(0.5)
    pinwheel2.rotate(45)
    pinwheels.add(pinwheel2)

    pinwheels2 = pinwheels.clone()
    pinwheels2.scale(0.5)
    pinwheels2.flip(0)
    pinwheels2.moveTo(600,250)

    pinterest.add(pinwheels)
    pinterest.add(pinwheels2)

    rects =  Canvas(800, 600, 'orange', 'Rectangles')
    rect = Rectangle(200,100)
    rect.setFillColor('blue')
    text = Text('Wrecked Angle', 20)
    text.setFontColor('white')
    namedRect= Layer()
    namedRect.add(rect)
    namedRect.add(text)
    namedRect.moveTo(300,400)
    rects.add(namedRect)
    namedRect2 = namedRect.clone()
    namedRect2.scale(2)
    namedRect2.moveTo(200,100)
    rects.add(namedRect2)
    unnamedRect = Rectangle(200,100, Point(600,200))
    unnamedRect.scale(1.5)
    unnamedRect.rotate(-30) # Can't rotate anything with text in it.
    rects.add(unnamedRect)


    objs = [tank, 
            circ,
            rect,
            Square(100, Point(200,300)),
            wedge,
            wedge2,
            path, 
            path2,                 
            Text('I wish I had a brain!', 12),
            # Image('glasses.gif'), # Comment out in case this image
                                    # isn't available
            Image(42,91), # Creates a blank 42x91 image  
            fish, 
            fish2,
            fish3, 
            pinterest,
            pinwheels,
            pinwheels2,

            namedRect,
            namedRect2,
            rects
            ]
    print("Test with printing contained objects turned off")
    for obj in objs:
        print('-'*50)
        printState(obj, False)
    print("Test with printing contained objects turned on")
    for obj in objs:
        print('-'*50)
        printState(obj, True)
        
if __name__=="__main__":
    testAll()
    
