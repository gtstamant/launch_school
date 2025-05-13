"""
## Problem:
- Determine whether triangle is equilateral, isosceles, or scalene

Requirements:
- Triangles have three sides > 0
- Sum of two sides must be > third side
- Triangle class
-- __init__ takes three sides
-- depending on side lengths, triangle.kind attribute set to string
   with triangle type
-- Invalid inputs raise ValueError


Questions:
- What information does it take in? Side lengths?
- Return a boolean value? Or triangle type?
- What to do if not a triangle
- Integer inputs? Floats okay?
- What if too many or too few sides given?

## Examples
See tests

## Data Structure
- Triangle class
- Triangle.kind attribute (or property?)
-- consider placing determination of type in separate functions?

## Algorithm

*Triangle Test*

Take three integer/float inputs
Sort the inputs into ascending order

**Validation**
if not all sides are > 0:
- raise ValueError

If the sum of first and second side is less than the third
- raise value error

**Determine Type**
If the first and third side are equal
- Set the "kind" attribute to "equilateral"

If the first and the second side are equal
- Set the "kind" attribute to "isosceles"

Otherwise:
- Set the "kind" attribute to "scalene"


"""
class Triangle:
    def __init__(self, *sides):
        self.sides = sorted(list(sides))
        if not self._validate_sides():
            raise ValueError('Invalid side lengths')

    def _validate_sides(self):
        return(
            all(side > 0 for side in self.sides) and
            sum(self.sides[:2]) > self.sides[2]
        )

    def _is_equilateral(self):
        return len(set(self.sides)) == 1
    
    def _is_scalene(self):
        return len(set(self.sides)) != 2
    
    @property
    def kind(self):
        if self._is_equilateral():
            return 'equilateral'
        if self._is_scalene():
            return 'scalene'
        
        return 'isosceles'