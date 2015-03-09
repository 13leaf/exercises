// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

// A random walker object!

class Walker {
  int x,y;

  Walker() {
    x = width/2;
    y = height/2;
  }

  void render() {
    stroke(0);
    strokeWeight(2);
    point(x,y);
  }

  // Randomly move up, down, left, right, or stay in one place
 void step() {
    
    float r = random(1);
    //70% go right,30% go left
    if(r<0.7){
      x++;
    }else{
      x--;
    }
    //60% down,40%up
    if(r<0.6){
      y++;
    }else{
      y--;
    }
  
    x = constrain(x,0,width-1);
    y = constrain(y,0,height-1);
  }
}
