// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

// A random walker object!

import java.util.*;

class Walker {
  int x,y;
  Random r;

  Walker() {
    x = width/2;
    y = height/2;
    r=new Random();
  }

  void render() {
    stroke(0);
    strokeWeight(2);
    point(x,y);
  }

  // Randomly move up, down, left, right, or stay in one place
 void step() {
   int xStep= (int)(r.nextGaussian()*4);
   int yStep= (int)(r.nextGaussian()*4);
   x=constrain(x+xStep,0,width);
   y=constrain(y+yStep,0,height);
  }
}
