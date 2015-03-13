Button button;
PFont myFont=createFont("Arial",20);
void setup()
{
  size(500, 500);
  button=new Button();
  button.label="click";
  button.setOnClickListener(new ButtonListener() {
    public void onClick() {
      println("clicked");
    }
  }
  );
}

void draw()
{
  button.draw();
  drawStatus();
  //println(mouseX+","+mouseY+"("+mouseButton+","+mousePressed+")");
}

String statusText="";
String lastStatus="";
void drawStatus()
{
  float fontSize=12;
  fill(#cecece);
  textFont(myFont, fontSize);
  text(statusText, 0, height-fontSize);
  if(lastStatus!=statusText){
    println(statusText);
    lastStatus=statusText;
  }
}

float offsetX=0;
float offsetY=0;

void mouseDragged()
{
  if (button.containsPoint(mouseX, mouseY)
    ) {
    button.x=mouseX+offsetX;
    button.y=mouseY+offsetY;
  }
  statusText="mouseDragged";
}

void mousePressed()
{
  if (button.containsPoint(mouseX, mouseY)
    ) {
    offsetX=button.x-mouseX;
    offsetY=button.y-mouseY;
    button.pressed=true;
  }
  statusText="mousePressed";
}

void mouseOut()
{
  statusText="mouseOut";
}

void mouseOver()
{
  statusText="mouseOver";
}

void mouseReleased()
{
  offsetX=0;
  offsetY=0;
  button.pressed=false;
  if (button.containsPoint(mouseX, mouseY)
    ) {
    button.click();
  }
  statusText="mouseReleased";
}

void mouseClicked()
{
  statusText="mouseClicked";
}

void mouseMoved()
{
  if (button.containsPoint(mouseX, mouseY)
    ) {
    button.hover=true;
  } else {
    button.hover=false;
  }
  statusText="mouseMoved";
}

class ButtonListener
{
  public void onClick() {
  }
}

class Button
{
  float x=0;
  float y=0;
  float w=200;
  float h=100;
  String label;
  boolean pressed=false;
  boolean hover=false;
  ButtonListener listener;

  public boolean containsPoint(float x, float y)
  {
    return x>=this.x && x<=this.x+this.w
      && y >=this.y && y<=this.y+this.h;
  }

  public void click()
  {
    if (this.listener != null) {
      listener.onClick();
    }
  }

  public void setOnClickListener(ButtonListener listener)
  {
    this.listener=listener;
  }

  public void draw()
  {
    //TODO button border,and border radius
    //TODO auto shrink button width when text overflow
    //TODO button texture
    background(255);
    stroke(hover?230:0);
    strokeWeight(2);
    fill(pressed?199:70);
    rect(x, y, w, h);
    fill(pressed?0:255);
    float fontSize=h/3;
    textFont(myFont, fontSize);
    text(label, (w-textWidth(label))/2+x, (h-fontSize)/2+y, w, h);
  }
}

