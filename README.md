# NMF Graphics

These Python scripts were used to generate the graphics for the video on [Source Separation using NMF](https://youtu.be/vc-WlAqv17c).

These Python scripts are based on the animation project [Manim](https://github.com/3b1b/manim) created by [3Blue1Brown](http://www.3blue1brown.com/about/).

The installation details can be found [here](https://talkingphysics.wordpress.com/2018/06/11/installing-manim-and-python-manim-series-part-1/) and a tutorial series on how to use this repository to make graphics can be found [here]( https://talkingphysics.wordpress.com/2018/06/11/learning-how-to-animate-videos-using-manim-series-a-journey/).

After cloning the Manim's repository, download these scripts into manim's parent directory (where the file extract_scene.py can be found). Now if the cloning and installation of dependencies have been done properly, the graphics can be generated using the command `python extract_scene.py <fileName>.py <requiredScene> -pl`. For example, the command `python extract_scene.py 4_proof.py ProofFNPart5_4 -pl` will generate and play the scene _ProofFNPart5_4_ of _4_proof.py_.
