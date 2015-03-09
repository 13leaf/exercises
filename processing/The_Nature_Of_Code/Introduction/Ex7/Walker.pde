class Walker {
  float x,y;
 
  float tx,ty;
 
  Walker() {
    tx = 0;
    ty = 10000;
    x=width/2;
    y=height/2;
  }
  
  void render() {
    stroke(0);
    strokeWeight(2);
    point(x,y);
  }
 
  void step() {
    float stepX = map(noise(tx), 0, 1, -5, 5);
    float stepY = map(noise(ty), 0, 1, -5, 5);
    
    x+=stepX;
    y+=stepY;
    x=constrain(x,0,width);
    y=constrain(y,0,height);
 
    tx += 0.01;
    ty += 0.01;
  }
}

