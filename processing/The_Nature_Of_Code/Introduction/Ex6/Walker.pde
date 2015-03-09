// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

// A random walker object!

class Walker {
  int x,y;
  float stepSize;

  Walker() {
    x = width/2;
    y = height/2;
    stepSize=random(1,2);
  }

  void render() {
    stroke(0);
    strokeWeight(2);
    point(x,y);
  }

  // Randomly move up, down, left, right, or stay in one place
 void step() {
  stepSize = constrain(random(stepSize*stepSize,stepSize*stepSize+0.1),0,40);
  println(stepSize);
  float stepx = random(-stepSize,stepSize);
  float stepy = random(-stepSize,stepSize);
 
  x += stepx;
  y += stepy;
  }
}
