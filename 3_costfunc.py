from big_ol_pile_of_manim_imports import *

class CostFunctionsModified(Scene):
	def construct(self):
		textTitle = TexMobject("""\\text{Cost Functions}""")
		textTitle.to_edge(UP)
		textTitle.set_color(BLUE)
		textTitle.scale(1.5)

		textVApproxWH = TexMobject("""{V}\\approx{W}{H}""")
		textVApproxWH.set_color(YELLOW)

		self.play(Write(textVApproxWH))
		self.wait(2)
		self.play(FadeIn(textTitle))
		self.wait(2)

		textFrobeniusNorm = TexMobject("""\\text{Frobenius Norm}""")
		textFrobeniusNorm.shift(2*UP)

		textFN_LHS = TexMobject("""\\left\\Vert A-B\\right\\Vert ^{2}""")
		textFN_LHS.set_color(YELLOW)

		textFNEqualTo = TexMobject("""=""")
		textFNEqualTo.set_color(YELLOW)
		textFNEqualTo.next_to(textFrobeniusNorm, DOWN)
		textFNEqualTo.shift(DOWN+LEFT)

		textFN_RHS = TexMobject("""\\sum_{ij}\\left(A_{ij}-B_{ij}\\right)^2""")
		textFN_RHS.set_color(YELLOW)

		textFN_LHS.next_to(textFNEqualTo, LEFT)
		textFN_RHS.next_to(textFNEqualTo, RIGHT)

		textKLDivergence = TextMobject("""Generalized KL Divergence""")
		textKLDivergence.next_to(textFNEqualTo, DOWN)
		textKLDivergence.shift(DOWN+RIGHT)

		textKLD_LHS = TexMobject("""D\\left(A||B\\right)""")
		textKLD_LHS.set_color(BLUE)

		textKLDEqualto = TexMobject("""=""")
		textKLDEqualto.set_color(BLUE)
		textKLDEqualto.next_to(textKLDivergence, DOWN)
		textKLDEqualto.shift(DOWN+2.5*LEFT)

		textKLD_RHS = TexMobject("""\\sum_{ij}\\left(A_{ij}\\log\\frac{A_{ij}}{B_{ij}}-A_{ij}+B_{ij}\\right)""")
		textKLD_RHS.set_color(BLUE)

		textKLD_LHS.next_to(textKLDEqualto, LEFT)
		textKLD_RHS.next_to(textKLDEqualto, RIGHT)

		self.play(FadeOut(textVApproxWH),
			FadeIn(textFrobeniusNorm),
			Write(textFN_LHS), Write(textFNEqualTo), Write(textFN_RHS),
			FadeIn(textKLDivergence), 
			Write(textKLD_LHS), Write(textKLDEqualto), Write(textKLD_RHS))
		self.wait(2)

		textFN_LHS_WH = TexMobject("""\\left\\Vert V-WH\\right\\Vert ^{2}""")
		textFN_LHS_WH.set_color(YELLOW)
		textFN_LHS_WH.next_to(textFNEqualTo, LEFT)

		textFN_RHS_WH = TexMobject("""\\sum_{ij}\\left(V_{ij}-\\left[WH\\right]_{ij}\\right)^2""")
		textFN_RHS_WH.set_color(YELLOW)
		textFN_RHS_WH.next_to(textFNEqualTo, RIGHT)

		textKLD_LHS_WH = TexMobject("""D\\left(V||WH\\right)""")
		textKLD_LHS_WH.set_color(BLUE)
		textKLD_LHS_WH.next_to(textKLDEqualto, LEFT)

		textKLD_RHS_WH = TexMobject("""\\sum_{ij}\\left(V_{ij}\\log\\frac{V_{ij}}{\\left[WH\\right]_{ij}}-V_{ij}+\\left[WH\\right]_{ij}\\right)""")
		textKLD_RHS_WH.set_color(BLUE)
		textKLD_RHS_WH.next_to(textKLDEqualto, RIGHT)

		self.wait(7)
		self.play(ReplacementTransform(textFN_LHS, textFN_LHS_WH),
			ReplacementTransform(textFN_RHS, textFN_RHS_WH),
			ReplacementTransform(textKLD_LHS, textKLD_LHS_WH),
			ReplacementTransform(textKLD_RHS, textKLD_RHS_WH))
		self.wait(3)

		textFN_RHS_zero = TexMobject("""0\\text{\\quad  when }V=WH""")
		textFN_RHS_zero.set_color(YELLOW)
		textFN_RHS_zero.next_to(textFNEqualTo, RIGHT)

		textKLD_RHS_zero = TexMobject("""0\\text{\\quad  when }V=WH""")
		textKLD_RHS_zero.set_color(BLUE)
		textKLD_RHS_zero.next_to(textKLDEqualto, RIGHT)

		self.play(FadeOut(textFN_RHS_WH), FadeIn(textFN_RHS_zero),
			FadeOut(textKLD_RHS_WH), FadeIn(textKLD_RHS_zero))
		self.wait(2.5)
		self.play(FadeOut(textFN_RHS_zero), FadeIn(textFN_RHS_WH),
			FadeOut(textKLD_RHS_zero), FadeIn(textKLD_RHS_WH))
		self.wait(10)
