// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com
//Find something you’ve previously made in Processing using separate x and y variables and use PVectors instead.
Walker w;

void setup() {
  size(800,200);
  // Create a walker object
  w = new Walker();
  background(255);
}

void draw() {
  // Run the walker object
  w.step();
  w.render();
}



