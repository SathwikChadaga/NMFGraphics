from big_ol_pile_of_manim_imports import *

class IntroScene(Scene):
	def construct(self):
		textTitleLine1 = TextMobject("""Source Separation using""")
		textTitleLine1.to_edge(UP)
		textTitleLine1.shift(DOWN)
		textTitleLine1.set_color(BLUE)
		textTitleLine1.scale(1.5)

		textTitleLine2 = TextMobject("""Non-negative Matrix Factorization""")
		textTitleLine2.next_to(textTitleLine1,2*DOWN)
		textTitleLine2.set_color(BLUE)
		textTitleLine2.scale(1.5)

		textAuthor1 = TextMobject("""Milind Kumar V, EE16B025""")
		textAuthor1.next_to(textTitleLine2, 6*DOWN)
		
		textAuthor2 = TextMobject("""Sathwik Chadaga P, EE15B113""")
		textAuthor2.next_to(textAuthor1, DOWN)

		self.play(FadeIn(textTitleLine1), FadeIn(textTitleLine2), FadeIn(textAuthor1), FadeIn(textAuthor2))
		self.wait(2)