float angle=0;
float step=3;
int direction=1;
boolean userControl=false;
int radius = 80;
float childRadius=15;
int fixedWidth=radius*3+radius/2;
WhiteBlankFactory factory=new WhiteBlankFactory();

ArrayList blanks=new ArrayList();

void setup()
{
  size(600, 800);
  frameRate(120);
  blanks.add(factory.newLeftFlat(-600));
  blanks.add(factory.newLeftFlat(-400));
  blanks.add(factory.newLeftFlat(-200));
  blanks.add(factory.newRightFlat(200));
  //blanks.add(factory.newLeftRect(200));
//  blanks.add(factory.newRightRect(400));
  //noLoop();
}

void keyPressed()
{
  if(keyCode == LEFT || key == 'a'){
      direction=-1;
      userControl=true;
  }else if(keyCode == RIGHT || key == 'd'){
      direction=1;
      userControl=true;
  }
}

void keyReleased()
{
  userControl=false;
}

void mousePressed()
{
  if(mouseX<width/2){
    direction=-1;
    userControl=true;
  }else{
    direction=1;
    userControl=true;  
  }
}

void mouseReleased()
{
  userControl=false;
}

void draw()
{
  background(0);

  for(int i=0;i<blanks.size();i++){
    blanks.get(i).step();
    blanks.get(i).display();
  }

  pushMatrix();
  stroke(250, 100);
  translate(width/2, height-radius-40);
  if(userControl){
    angle=(angle+step*direction)%360;  
  }
  rotate(radians(angle));
  noFill();
  ellipse(0, 0, radius*2, radius*2);

  noStroke();
  fill(0, 0, 255);
  ellipse(-radius, 0, childRadius*2, childRadius*2);
  fill(255, 0, 0);
  ellipse(radius, 0, childRadius*2, childRadius*2);

  popMatrix();

}

