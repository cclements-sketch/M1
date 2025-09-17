# M1

## Title: Markov Roadtrip

## Description

This project generates a natural landscape as a Markov chain using a transition matrix. Just like in real life, certain biomes are likely to appear next to one another, while others have a much lower probability of appearing near each other. Possible biomes include mountains and hills of different sizes in addition to mountains, lakes, and deserts. Users can drive through the landscape in a virtual car.

## Setup

Download both images in the **assets** folder locally. Open **markov_roadtrip.py** in a Python editor and delete lines 25-29. Replace them with the following:
```
CAR = os.path.expanduser("path_to_your_local_car_drawing.gif")
FLIPPEDCAR = os.path.expanduser("path_to_your_local_car_drawing_flipped.gif")
```
Next, run the code. You can press the right arrow key to drive to the right. Once you reach the righthand edge of the canvas, you can press the left arrow key to drive to the left.

## Personal value

I have always loved being in nature. When I was a kid, my family would take road trips through beautiful natural areas, hiking and camping along the way. These trips sparked my curiosity about different ecosystems. When I arrived at Bowdoin, I planned to major in biology, but learned that I prefer coding to working in a biology lab. Currently, I am looking for ways to combine math, computer science, and biology. Creating **Markov Roadtrip** was fun because I could experiment with adjusting the transition matrix so that biomes would appear next to one another in a way that seemed realistic and aesthetically pleasing. When I look at the generated landscapes, I am reminded of the sense of awe I felt when looking at tall mountains or national forests out of a car window.

## Challenges along the way

Although I enjoy drawing freehand, I have little experience with computer graphics. In order to create many of the biomes for this project, I had to make example sketches on paper and then calculate distances and angles. It took a lot of patience, but in the end, I think I succeeded in making drawings that are simple and easy to interpret. Another aspect of the project that challenged me was user interaction. I have done mostly backend programming and data analysis, and have not had the change to experiment much with web design or video games. It was difficult for me to think of an intuitive way for the user to navigate generated landscapes. I also spent a long time eliminating bugs that detracted from the user experience, such as the car's flickering motion. These challenges were important because it is hard for me to push myself out of my comfort zone on assignments. Finishing this assignment helped me prove to myself that I am capable of learning a tool that I have not used much (Turtle graphics), and looking through documentation when I got stuck on problems. In the future, I definitely want to learn more about computer graphics. I will be more aware of the user interaction aspects of my projects.

## Creativity

I think that my system is a little bit creative, but not as creative as something like a novel solution to an important problem. The visual art that the system generates has some value to me because it brings back memories. I do not think it has much value to humanity in general, because it does not really advance any field of knowledge. I also believe that in the sense that the generated landscapes are creative, my exploratory creativity plays a bigger part than the program's combinatorial creativity. My exploratory creativity is responsible for the project idea, biome and car designs, and interactivity. The program's combinatorial creativity simply combines the biomes that I designed in novel ways.

## Sources

Python Software Foundation. Python Language Reference, version 3.13.7. Available at http://www.python.org

https://stackoverflow.com/a/6049340

https://stackoverflow.com/a/55669350

https://stackoverflow.com/a/60130696

https://stackoverflow.com/a/55895481
