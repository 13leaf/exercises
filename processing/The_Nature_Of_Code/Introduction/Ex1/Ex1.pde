// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com
//EX: Create a random walker that has a tendency to move down and to the right. (We’ll see the solution to this in the next section.)

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


