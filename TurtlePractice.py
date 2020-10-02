import turtle
import random
"""
Helpful functions:
    turtle.forward(dist)    or turtle.fd(dist)
    turtle.right(deg)       of turtle.rt(deg)
    turtle.left(deg)        or turtle.lt(deg)
Creating a turtle:
    myTurtle = turtle.Turtle()
    #now you can use this instead of 'turtle.'
    myTurtle.fd(20)
    
docs: https://docs.python.org/3.3/library/turtle.html?highlight=turtle#module-turtle
"""


def m(myTurtle):
  myTurtle.lt(70);
  myTurtle.fd(100);
  myTurtle.rt(140)
  myTurtle.fd(65)
  myTurtle.lt(140);
  myTurtle.fd(65);
  myTurtle.rt(140);
  myTurtle.fd(100);
  myTurtle.lt(70);
  
def i(myTurtle):
  myTurtle.lt(90)
  myTurtle.fd(90);
  myTurtle.lt(90);
  myTurtle.fd(45);
  myTurtle.rt(180);
  myTurtle.fd(90);
  myTurtle.lt(180);
  myTurtle.fd(45);
  myTurtle.lt(90);
  myTurtle.fd(90);
  myTurtle.rt(90);
  myTurtle.fd(45);
  myTurtle.lt(180);
  myTurtle.fd(90);

def y(myTurtle):
  myTurtle.penup();
  myTurtle.lt(90);
  myTurtle.fd(90);
  myTurtle.rt(135);
  myTurtle.pendown();
  myTurtle.fd(45);
  myTurtle.lt(90);
  myTurtle.fd(45);
  myTurtle.rt(180);
  myTurtle.fd(45);
  myTurtle.lt(45);
  myTurtle.fd(60);
  myTurtle.lt(90);
  myTurtle.penup();
  myTurtle.fd(45);

def a(myTurtle):
  myTurtle.lt(70);
  myTurtle.fd(120)
  myTurtle.rt(70);
  myTurtle.fd(30);
  myTurtle.rt(70);
  myTurtle.fd(120);
  myTurtle.rt(180);
  myTurtle.fd(70);
  myTurtle.lt(70);
  myTurtle.fd(65);
  myTurtle.rt(180);
  myTurtle.fd(65);
  myTurtle.rt(70);
  myTurtle.fd(70);
  myTurtle.lt(70);
def d(myTurtle):

  myTurtle.circle(80,180)
  myTurtle.lt(90);
  myTurtle.fd(160);
  myTurtle.penup();
  myTurtle.lt(90);
  myTurtle.fd(80);

def p(myTurtle):

  myTurtle.circle(40,180)
  myTurtle.lt(90);
  myTurtle.fd(160);
  myTurtle.penup();
  myTurtle.lt(90);
  myTurtle.fd(40);
def n(myTurtle):
 
  myTurtle.lt(80);
  myTurtle.fd(100);
  myTurtle.rt(150)
  myTurtle.fd(100)
  myTurtle.lt(150);
  myTurtle.fd(100);
  myTurtle.penup();
  myTurtle.lt(200);
  myTurtle.fd (100);
  myTurtle.lt(80);

def e(myTurtle):
  myTurtle.penup();
  myTurtle.lt(90);
  myTurtle.fd(120);
  myTurtle.rt(90);
  myTurtle.pendown();
  myTurtle.fd(60);
  myTurtle.rt(180);
  myTurtle.fd(60);
  myTurtle.lt(90);
  myTurtle.fd(60);
  myTurtle.lt(90);
  myTurtle.fd(60);
  myTurtle.lt(180);
  myTurtle.fd(60);
  myTurtle.lt(90);
  myTurtle.fd(60);
  myTurtle.lt(90);
  myTurtle.fd(60);

def r(myTurtle):
  myTurtle.penup();
  myTurtle.lt(90);
  myTurtle.fd(80);
  myTurtle.rt(90);
  myTurtle.pendown();
  myTurtle.circle(40,180)
  myTurtle.lt(90);
  myTurtle.fd(160);
  myTurtle.lt(180);
  myTurtle.fd(80);
  myTurtle.rt(140);
  myTurtle.fd(105);

##this thing is terrifying
def smile(myTurtle):
  myTurtle.penup();
  myTurtle.fd(60);
  myTurtle.pendown();
  myTurtle.circle(20, 360);
  myTurtle.penup();
  myTurtle.rt(180);
  myTurtle.fd(120);
  myTurtle.rt(90)
  myTurtle.fd(20)
  myTurtle.pendown();
  myTurtle.circle(20,360);
  myTurtle.penup();
  myTurtle.lt(90);
  myTurtle.fd(40);
  myTurtle.lt(90)
  myTurtle.fd(70);
  myTurtle.pendown();
  myTurtle.circle(90, 180);


def main():
    myTurtle = turtle.Turtle()
    myTurtle.reset();
    myTurtle.hideturtle();
    
    input_flag = 0;
    while (input_flag == 0):
      word_count = input("Please enter a positive integer for number of words to generate.");
      if (word_count.find("-") != -1):
        print ("error: POSITIVE integers only.");
      elif (word_count.find("-") == -1):
        for ch in word_count:
          if (ch >= "0" and ch <= "9"):
            input_flag = 1;
          else: 
            print ("Error: Positive INTEGERS only.")
      if (input_flag == 1):
        for x in range (int(word_count)):
          num_gen = random.randint(1,5);
          if (num_gen == 1):
            m(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();
            i(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();
            y(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();
            a(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();

          elif (num_gen == 2):
            m(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();
            a(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();
            d(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();

          elif (num_gen == 3):
            p(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();
            a(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();
            i(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();
            d(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();

          elif (num_gen == 4):
            d(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();
            i(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();
            n(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();
            e(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();
            r(myTurtle);
            myTurtle.penup();
            myTurtle.fd(40);
            myTurtle.pendown();
          elif (num_gen==5):
            smile(myTurtle);

          myTurtle.reset();
        input_flag = 1;

# These lines handle calling main, if main should be called
if __name__ == '__main__':
    main()
else:
  # This would be weird
  pass
