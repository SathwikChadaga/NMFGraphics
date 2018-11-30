from big_ol_pile_of_manim_imports import *

#_______ Intro ________

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

#_______ NMF ________

class NMFIntro(Scene):
	def construct(self):
		textNMFTitle = TexMobject("""\\text{Non-negative Matrix Factorization}""")
		textNMFTitle.to_edge(UP)
		textNMFTitle.set_color(BLUE)
		textNMFTitle.scale(1.5)

		textMathEqualtoFrist = TexMobject("""{=}""")
		textMathEqualtoFrist.set_color(YELLOW)
		textMathEqualtoFrist.shift(UP+2*LEFT)

		textMathV = TexMobject("""{V}_{{m}\\times{n}}""")
		textMathV.set_color(YELLOW)
		textMathV.next_to(textMathEqualtoFrist, LEFT)


		matrixMathV = TexMobject("""
        \\left[
            \\begin{array}{cccc}
                {V}_{11} & \\hdots & \\hdots & {V}_{1n} \\\\
                \\vdots & \\hdots & \\hdots & \\hdots  \\\\
                \\vdots & \\hdots & \\hdots & \\hdots  \\\\
                {V}_{m1} & \\hdots & \\hdots & {V}_{mn}
            \\end{array}
        \\right]
        """)
		matrixMathV.next_to(textMathEqualtoFrist, RIGHT)
		matrixMathV.set_color(YELLOW)
		matrixMathV.scale(0.8)

		matrixMathWH = TexMobject("""
        \\left[
            \\begin{array}{ccc}
                {W}_{11} & \\hdots & {W}_{1r}  \\\\
                \\vdots & \\hdots & \\hdots   \\\\
                \\vdots & \\hdots & \\hdots   \\\\
                {W}_{m1} & \\hdots & {W}_{mr}
            \\end{array}
        \\right]
        \\left[
            \\begin{array}{cccc}
                {H}_{11} & \\hdots & \\hdots & {H}_{1n} \\\\
                \\vdots & \\hdots & \\hdots & \\hdots  \\\\
                {H}_{r1} & \\hdots & \\hdots & {H}_{rn}
            \\end{array}
        \\right]
        """)

		textCondV = TexMobject("""\\begin{array}{c}
			V_{ij}\\geq0\\\\
			1\\leq i\\leq m\\\\
			1\\leq j\\leq n
			\\end{array}""")
		textCondV.next_to(matrixMathV,4*DOWN)
		textCondV.scale(0.8)

		self.play(FadeIn(textNMFTitle))
		self.wait(4)
		self.play(Write(textMathV),Write(textMathEqualtoFrist), Write(matrixMathV))
		self.wait(2)
		self.play(FadeIn(textCondV))
		self.wait(1)
		self.play(FadeOut(textMathV), FadeOut(textMathEqualtoFrist),
			ApplyMethod(matrixMathV.to_edge,LEFT))

		textMathEqualtoSecond = TexMobject("""{=}""")
		textMathEqualtoSecond.set_color(YELLOW)
		textMathEqualtoSecond.next_to(matrixMathV, RIGHT)


		textMathWH = TexMobject("""{{W}_{{m}\\times{r}}{H}_{{r}\\times{n}}}""")
		textMathWH.set_color(YELLOW)
		textMathWH.next_to(textMathEqualtoSecond, RIGHT)
		textMathWH.shift(2*RIGHT)

		matrixMathWH.set_color(YELLOW)
		matrixMathWH.scale(0.8)
		matrixMathWH.next_to(textMathEqualtoSecond, RIGHT)

		textCondW = TexMobject("""\\begin{array}{c}
			W_{ij}\\geq0\\\\
			1\\leq i\\leq m\\\\
			1\\leq j\\leq r
			\\end{array}""")
		textCondW.next_to(matrixMathWH,4*DOWN)
		textCondW.shift(2*LEFT)
		textCondW.scale(0.8)

		textCondH = TexMobject("""\\begin{array}{c}
			H_{ij}\\geq0\\\\
			1\\leq i\\leq r\\\\
			1\\leq j\\leq n
			\\end{array}""")
		textCondH.next_to(matrixMathWH, 4*DOWN)
		textCondH.shift(2*RIGHT)
		textCondH.scale(0.8)

		self.play(Write(textMathEqualtoSecond), Write(textMathWH),
			ApplyMethod(textCondV.move_to, matrixMathV.get_corner(DOWN)+1.8*DOWN))
		self.wait(1)
		self.play(ReplacementTransform(textMathWH, matrixMathWH))
		self.wait(0.5)
		self.play(FadeIn(textCondW))
		self.play(FadeIn(textCondH))

		textNotUnique = TexMobject("""\\text{Not unique}""")
		textNotUnique.to_edge(DOWN)
		textNotUnique.set_color(YELLOW)

		self.play(FadeIn(textNotUnique))
		self.wait(5)

class ColumnwiseMultPart1(Scene):
	def construct(self):
		matrixV = TexMobject("""\\text{V}""")
		matrixV.shift(3*LEFT)

		textEqualTo = TexMobject("""\\text{=}""")
		textEqualTo.next_to(matrixV, RIGHT)
		
		matrixW = TexMobject("""\\text{W}""")
		matrixW.next_to(textEqualTo, RIGHT)

		textTimes = TexMobject("""\\times""")
		textTimes.next_to(matrixW, RIGHT)
		
		matrixH = TexMobject("""\\text{H}""")
		matrixH.next_to(textTimes, RIGHT)
		
		matrixExpanded = TexMobject("""
        \\left[
            \\begin{array}{ccc}
                {H}_{1} & {H}_{2} & {H}_{3} \\\\
                \\vdots  & \\vdots  & \\vdots  \\\\
                \\vdots  & \\vdots  & \\vdots 
            \\end{array}
        \\right]
        """)
		matrixExpanded.next_to(textTimes, RIGHT)
		
		self.play(FadeIn(matrixV), FadeIn(textEqualTo),
			FadeIn(matrixW), FadeIn(textTimes), FadeIn(matrixH))
		self.play(Transform(matrixH, matrixExpanded))

		matrixWCopy1 = TexMobject("""\\text{W}""")
		matrixWCopy1.next_to(matrixExpanded, LEFT, buff = -2.8)
		
		matrixWCopy2 = TexMobject("""\\text{W}""")
		matrixWCopy2.next_to(matrixExpanded, LEFT, buff = -1.6)

		matrixWCopy3 = TexMobject("""\\text{W}""")
		matrixWCopy3.next_to(matrixExpanded, LEFT, buff = -0.5)

		self.play( Transform(matrixW.copy(), matrixWCopy1), Transform(matrixW.copy(), matrixWCopy2), Transform(matrixW, matrixWCopy3), FadeOut(textTimes))

class ColumnwiseMultPart2(Scene):
	def construct(self):
		matrixV = TexMobject("""\\text{V}""")
		matrixV.shift(3*LEFT)

		textEqual = TexMobject("""\\text{=}""")
		textEqual.next_to(matrixV,RIGHT)

		matrixW = TexMobject("""\\text{W}""")
		matrixW.next_to(textEqual,RIGHT)

		textTimes = TexMobject("""\\times""")
		textTimes.next_to(matrixW,RIGHT)

		matrixExpanded = TexMobject("""
        \\left[
            \\begin{array}{ccc}
                {H}_{1} & {H}_{2} & {H}_{3} \\\\
                \\vdots  & \\vdots  & \\vdots  \\\\
                \\vdots  & \\vdots  & \\vdots 
            \\end{array}
        \\right]
        """)
		matrixExpanded.next_to(textTimes,RIGHT)

		matrixWCopy1 = TexMobject("""\\text{W}""")
		matrixWCopy1.next_to(matrixExpanded, LEFT, buff = -2.8)

		matrixWCopy2 = TexMobject("""\\text{W}""")
		matrixWCopy2.next_to(matrixExpanded, LEFT, buff = -1.6)

		matrixWCopy3 = TexMobject("""\\text{W}""")
		matrixWCopy3.next_to(matrixExpanded, LEFT, buff = -0.5)

		self.add(matrixV)
		self.add(textEqual)
		self.add(matrixExpanded)
		self.add(matrixWCopy1)
		self.add(matrixWCopy2)
		self.add(matrixWCopy3)

		matrixWH = TexMobject("""
        \\left[
            \\begin{array}{ccc}
                {W}\\times{H}_{1} & {W}\\times{H}_{2} & {W}\\times{H}_{3} \\\\
                \\vdots  & \\vdots  & \\vdots  \\\\
                \\vdots  & \\vdots  & \\vdots 
            \\end{array}
        \\right]
        """)
		matrixWH.next_to(textEqual,RIGHT)
		
		self.play(FadeIn(matrixWH), FadeOut(matrixExpanded), FadeOut(matrixWCopy1), FadeOut(matrixWCopy2), FadeOut(matrixWCopy3))

class ColumnwiseMultPart3(Scene):
	def construct(self):
		matrixV = TexMobject("""\\text{V}""")
		matrixV.shift(3*LEFT)

		textEqual = TexMobject("""\\text{=}""")
		textEqual.next_to(matrixV,RIGHT)

		matrixWH = TexMobject("""
        \\left[
            \\begin{array}{ccc}
                {W}\\times{H}_{1} & {W}\\times{H}_{2} & {W}\\times{H}_{3} \\\\
                \\vdots  & \\vdots  & \\vdots  \\\\
                \\vdots  & \\vdots  & \\vdots 
            \\end{array}
        \\right]
        """)
		matrixWH.next_to(textEqual,RIGHT)

		self.add(matrixV)
		self.add(textEqual)
		self.add(matrixWH)
		self.play(ApplyMethod(textEqual.shift,RIGHT), ApplyMethod(matrixWH.shift,RIGHT))

		matrixVExpanded = TexMobject("""
        \\left[
            \\begin{array}{ccc}
                {V}_{1} & {V}_{2} & {V}_{3} \\\\
                \\vdots  & \\vdots  & \\vdots  \\\\
                \\vdots  & \\vdots  & \\vdots 
            \\end{array}
        \\right]
        """)
		matrixVExpanded.next_to(textEqual,LEFT)
        
		self.play(Transform(matrixV,matrixVExpanded))

class ColumnwiseMultPart4(Scene):
    def construct(self):
        matrixV = TexMobject("""\\text{V}""")
        matrixV.shift(3*LEFT)

        textEqual = TexMobject("""\\text{=}""")
        textEqual.next_to(matrixV,RIGHT)

        matrixWH = TexMobject("""
        \\left[
            \\begin{array}{ccc}
                {W}\\times{H}_{1} & {W}\\times{H}_{2} & {W}\\times{H}_{3} \\\\
                \\vdots  & \\vdots  & \\vdots  \\\\
                \\vdots  & \\vdots  & \\vdots 
            \\end{array}
        \\right]
        """)
        matrixWH.next_to(textEqual,RIGHT)

        textEqual.shift(RIGHT)
        matrixWH.shift(RIGHT)

        matrixVExpanded = TexMobject("""
        \\left[
            \\begin{array}{ccc}
                {V}_{1} & {V}_{2} & {V}_{3} \\\\
                \\vdots  & \\vdots  & \\vdots  \\\\
                \\vdots  & \\vdots  & \\vdots 
            \\end{array}
        \\right]
        """)
        matrixVExpanded.next_to(textEqual,LEFT)
        
        self.add(matrixVExpanded, matrixWH, textEqual)

        vectorWH = TexMobject("""
        \\left[
            \\begin{array}{c}
                {W}\\times{H}_{j} \\\\
                \\vdots  \\\\
                \\vdots  
            \\end{array}
        \\right]
        """)
        vectorWH.next_to(textEqual,RIGHT)

        vectorV = TexMobject("""
        \\left[
            \\begin{array}{ccc}
                {V}_{j}  \\\\
                \\vdots   \\\\
                \\vdots 
            \\end{array}
        \\right]
        """)
        vectorV.next_to(textEqual,LEFT)

        self.play(Transform(matrixVExpanded,vectorV), Transform(matrixWH,vectorWH))

class ColumnwiseMultPart5(Scene):
	def construct(self):
		textV = TexMobject("""\\text{V}""")
		textV.shift(3*LEFT)

		textEqual = TexMobject("""\\text{=}""")
		textEqual.next_to(textV,RIGHT)
		textEqual.shift(RIGHT)

		vectorV = TexMobject("""
        \\left[
            \\begin{array}{ccc}
                {V}_{1}  \\\\
                \\vdots   \\\\
                \\vdots 
            \\end{array}
        \\right]
        """)
		vectorV.next_to(textEqual,LEFT)

		vectorWH = TexMobject("""
        \\left[
            \\begin{array}{c}
                {W}\\times{H}_{1} \\\\
                \\vdots  \\\\
                \\vdots 
            \\end{array}
        \\right]
        """)
		vectorWH.next_to(textEqual,RIGHT)

		self.add(vectorV,textEqual,vectorWH)
		self.wait(2)

		vectorVj = TexMobject("""
        \\left[
            \\begin{array}{ccc}
                {V}_{j}  \\\\
                \\vdots   \\\\
                \\vdots 
            \\end{array}
        \\right]
        """)
		vectorVj.next_to(textEqual,LEFT)

		vectorWHj = TexMobject("""
        \\left[
            \\begin{array}{c}
                {W}\\times{H}_{j} \\\\
                \\vdots  \\\\
                \\vdots 
            \\end{array}
        \\right]
        """)
		vectorWHj.next_to(textEqual,RIGHT)

		self.play(Transform(vectorV,vectorVj), Transform(vectorWH,vectorWHj))
		self.wait(2)

class ColumnwiseMultPart6(Scene):
	def construct(self):
		textV = TexMobject("""\\text{V}""")
		textV.shift(3*LEFT)

		textEqual = TexMobject("""\\text{=}""")
		textEqual.next_to(textV,RIGHT)
		textEqual.shift(RIGHT)

		vectorV = TexMobject("""
        \\left[
            \\begin{array}{ccc}
                {V}_{j}  \\\\
                \\vdots   \\\\
                \\vdots 
            \\end{array}
        \\right]
        """)
		vectorV.next_to(textEqual,LEFT)

		vectorWH = TexMobject("""
        \\left[
            \\begin{array}{c}
                {W}\\times{H}_{j} \\\\
                \\vdots  \\\\
                \\vdots 
            \\end{array}
        \\right]
        """)
		vectorWH.next_to(textEqual,RIGHT)

		self.add(vectorV,textEqual,vectorWH)

		textVj = TexMobject("""{V(:,j)}""")
		textVj.next_to(textEqual,LEFT)
		textWHj = TexMobject("""\\text{W}\\times{H(:,j)""")
		textWHj.next_to(textEqual,RIGHT)

		self.play(Transform(vectorV,textVj), Transform(vectorWH,textWHj))

class ColumnPicturePart1(Scene):
	def construct(self):

		textColPic = TexMobject("""\\text{Using column picture of matrix multiplication,}""")
		textColPic.set_color_by_tex_to_color_map({
		"column picture": YELLOW
		})
		textColPic.to_edge(UP)

		textV = TexMobject("""\\text{V}""")
		textV.next_to(textColPic, DOWN)
		textV.shift(3*LEFT+0.5*DOWN)

		textEqual = TexMobject("""\\text{=}""")
		textEqual.next_to(textV,RIGHT)
		textEqual.shift(RIGHT)

		textVj = TexMobject("""{V(:,j)}""")
		textVj.next_to(textEqual,LEFT)

		textWHj = TexMobject("""\\text{W}\\times{H(:,j)""")
		textWHj.next_to(textEqual,RIGHT)

		textNewEqual = TexMobject("""\\text{=}""")
		textNewEqual.next_to(textVj,RIGHT+3*DOWN)

		textSumWHj = TexMobject("""\\sum_{k=1}^{r} {W(:,k)}\\times{H(k,j)}""")
		textSumWHj.next_to(textNewEqual,RIGHT)

		self.play(FadeIn(textVj), FadeIn(textWHj), FadeIn(textEqual))
		self.play(FadeIn(textColPic))
		self.play(FadeIn(textNewEqual), FadeIn(textSumWHj))

		textSourceComp = TexMobject("""j^{\\text{th}}\\text{ source}=\\sum_{k=1}^{r} \\left({k}^{\\text{th}}\\text{ component}\\right)""")
		textSourceComp.next_to(textColPic, DOWN)
		textSourceComp.shift(3*DOWN)
		textSourceComp.set_color(GREEN)

		textEncoder = TexMobject("""\\times\\left(\\text{encoder of }{k}^{\\text{th}}\\text{component in }j^{\\text{th}}\\text{ source}\\right)""")
		textEncoder.next_to(textSourceComp, DOWN)
		textEncoder.set_color(GREEN)

		textSourceComp.shift(LEFT)
		textEncoder.shift(RIGHT)

		self.play(FadeIn(textSourceComp), FadeIn(textEncoder))

class ColumnPicturePart2(Scene):
	def construct(self):
		textV = TexMobject("""\\text{V}""")
		textV.shift(3*LEFT)

		textEqual = TexMobject("""\\text{=}""")
		textEqual.next_to(textV,RIGHT)
		textEqual.shift(RIGHT)

		textVj = TexMobject("""{V(:,j)}""")
		textVj.next_to(textEqual,LEFT)

		textNewEqual = TexMobject("""\\text{=}""")
		textNewEqual.next_to(textVj,RIGHT+3*DOWN)

		textSumWHj = TexMobject("""\\sum_{k=1}^{r} {W(:,k)}\\times{H(k,j)}""")
		textSumWHj.next_to(textNewEqual,RIGHT)

		textColPic = TexMobject("""\\text{Using column picture of matrix multiplication,}""")
		textColPic.set_color_by_tex_to_color_map({
		"column picture": YELLOW
		})
		textColPic.to_edge(TOP)

		self.add(textVj, textSumWHj, textNewEqual, textColPic)
		self.play(ApplyMethod(textSumWHj.shift,UP), ApplyMethod(textNewEqual.shift,UP))

#_______ Cost Function ________

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

#_______ Proof ________

class ProofFNPart5_1(Scene):
	def construct(self):
		textTitle = TexMobject("""\\text{Multiplicative Update Rules}""")
		textTitle.set_color(BLUE)
		textTitle.scale(1.5)
		textTitle.to_edge(UP)

		textFh = TexMobject("""{F(h)=\\frac{1}{2}\\sum_{i}(v_{i}-\\sum_{j}W_{ij}h_{j})^{2}}""")
		textFh.next_to(textTitle, DOWN)
		textFh.set_color(YELLOW)

		self.play( FadeIn(textTitle))
		self.wait(3)
		self.play( FadeIn(textFh))
		self.wait(3)

class ProofFNPart5_2(Scene):
	def construct(self):
		textTitle = TexMobject("""\\text{Multiplicative Update Rules}""")
		textTitle.set_color(BLUE)
		textTitle.scale(1.5)
		textTitle.to_edge(UP)

		textFh = TexMobject("""{F(h)=\\frac{1}{2}\\sum_{i}(v_{i}-\\sum_{j}W_{ij}h_{j})^{2}}""")
		textFh.next_to(textTitle, DOWN)
		textFh.set_color(YELLOW)
		
		textFhQuadratic = TexMobject("""{F(h)}\\text{ is quadratic. It is Taylor Series expanded as}""")
		textFhQuadratic.next_to(textFh, DOWN)

		textTaylorExpLine1 = TexMobject("""F(h)=F(h_{t})+(h-h_{t})^{T}\\nabla F(h_{t})""")
		textTaylorExpLine1.next_to(textFhQuadratic, DOWN)
		textTaylorExpLine1.set_color(YELLOW)
		textTaylorExpLine1.scale(0.9)

		textTaylorExpLine2 = TexMobject("""+\\frac{1}{2}(h-h_{t})^{T}\\left(W^{T}W\\right)(h-h_{t})""")
		textTaylorExpLine2.next_to(textTaylorExpLine1, DOWN)
		textTaylorExpLine2.set_color(YELLOW)
		textTaylorExpLine2.shift(RIGHT)
		textTaylorExpLine2.scale(0.9)

		textTaylorExpLine1.shift(LEFT)

		self.add(textTitle)
		self.add(textFh)
		self.play(FadeIn(textFhQuadratic))
		self.wait(2)
		self.play(FadeIn(textTaylorExpLine1), FadeIn(textTaylorExpLine2))
		self.wait(2)

class ProofFNPart5_3(Scene):
	def construct(self):
		textTitle = TexMobject("""\\text{Multiplicative Update Rules}""")
		textTitle.set_color(BLUE)
		textTitle.scale(1.5)
		textTitle.to_edge(UP)

		textFh = TexMobject("""{F(h)=\\frac{1}{2}\\sum_{i}(v_{i}-\\sum_{j}W_{ij}h_{j})^{2}}""")
		textFh.next_to(textTitle, DOWN)
		textFh.set_color(YELLOW)
		
		textFhQuadratic = TexMobject("""{F(h)}\\text{ is quadratic. It is Taylor Series expanded as}""")
		textFhQuadratic.next_to(textFh, DOWN)

		textTaylorExpLine1 = TexMobject("""F(h)=F(h_{t})+(h-h_{t})^{T}\\nabla F(h_{t})""")
		textTaylorExpLine1.next_to(textFhQuadratic, DOWN)
		textTaylorExpLine1.set_color(YELLOW)
		textTaylorExpLine1.scale(0.9)

		textTaylorExpLine2 = TexMobject("""+\\frac{1}{2}(h-h_{t})^{T}\\left(W^{T}W\\right)(h-h_{t})""")
		textTaylorExpLine2.next_to(textTaylorExpLine1, DOWN)
		textTaylorExpLine2.set_color(YELLOW)
		textTaylorExpLine2.shift(RIGHT)
		textTaylorExpLine2.scale(0.9)

		textTaylorExpLine1.shift(LEFT)

		textDefineAux = TexMobject("""\\text{We define auxiliary function }{G(h,h_{t})}\\text{ such that}""")
		textDefineAux.next_to(textTaylorExpLine2, DOWN)
		textDefineAux.shift(LEFT)

		textAuxGhhtCond1 = TexMobject("""G(h,h_{t})\\geq F(h)""")
		textAuxGhhtCond1.next_to(textDefineAux, DOWN)
		textAuxGhhtCond1.set_color(YELLOW)

		textAuxGhhtCond2 = TexMobject("""G(h_{t},h_{t})=F(h_{t})""")
		textAuxGhhtCond2.next_to(textAuxGhhtCond1, DOWN)
		textAuxGhhtCond2.set_color(YELLOW)

		self.add(textTitle)
		self.add(textFh)
		self.add(textFhQuadratic)
		self.add(textTaylorExpLine1)
		self.add(textTaylorExpLine2)
		self.play(FadeIn(textDefineAux))
		self.wait(1.5)
		self.play(FadeIn(textAuxGhhtCond1), FadeIn(textAuxGhhtCond2))
		self.wait(4.5)

class ProofFNPart5_4(GraphScene):
    CONFIG = {
    "x_min" : -3.5,
    "x_max" : 6.5,
    "y_min" : 0,
    "y_max" : 70,
    "x_axis_label": "$h$",
    "y_tick_frequency": 10,
    "graph_origin" : ORIGIN ,
    "function_color" : RED ,
    "axes_color" : GREEN,
    "graph_origin": 3*DOWN+LEFT,
    "axes_color": GREY
    }
    
    def construct(self):
        self.setup_axes(animate=True) 

        graphFh =self.get_graph(self.functionForGraph1,self.function_color)
        graphGhht =self.get_graph(self.functionForGraph2)
        graphGhhtPlusOne =self.get_graph(self.functionForGraph3)

        vertLine0 = self.get_vertical_line_to_graph(-3.5+1.5,graphFh,color=YELLOW)
        vertLine1 = self.get_vertical_line_to_graph(-2+1.5,graphGhht,color=YELLOW)
        vertLine2 = self.get_vertical_line_to_graph(-2+1.5,graphFh,color=YELLOW)
        vertLine3 = self.get_vertical_line_to_graph(-1+1.5,graphGhhtPlusOne,color=YELLOW)
        vertLine4 = self.get_vertical_line_to_graph(-1+1.5,graphFh,color=YELLOW)
        vertLine5 = self.get_vertical_line_to_graph(1.5,graphFh,color=YELLOW)

        text_ht = TexMobject("{h}_{t}")
        text_htPlus1 = TexMobject("{h}_{t+1}")
        text_htPlus2 = TexMobject("{h}_{t+2}")
        text_htMin = TexMobject("{h}_{min}")

        graphLabel1 = self.get_graph_label(graphFh, x_val=6, label = "{F(h)}")
        graphLabel2 =self.get_graph_label(graphGhht,x_val=1, label = "{G(h,h^t)}")
        graphLabel3 =self.get_graph_label(graphGhhtPlusOne, x_val=1.5, label = "{G(h,{h}^{t+1})}")

        arrow = Arrow(np.array([-0.6,-1.6,0]),np.array([0.5,-2.1,0]))
        
        self.play(ShowCreation(graphFh))
        self.play(ShowCreation(graphLabel1))
        self.play(ShowCreation(graphGhht))
        self.play(ShowCreation(graphLabel2))

        text_ht.next_to(vertLine0, DOWN)
        
        self.play(ShowCreation(vertLine0),ShowCreation(text_ht))
        
        text_htPlus1.next_to(vertLine1, DOWN)
        
        self.play(ShowCreation(vertLine1),ShowCreation(text_htPlus1))
        self.play(FadeOut(vertLine0), FadeOut(text_ht))
        self.add(vertLine2)
        self.play(FadeOut(graphGhht),FadeOut(vertLine1),FadeOut(graphLabel2))
        self.play(ShowCreation(graphGhhtPlusOne))
        self.play(ShowCreation(graphLabel3))
        
        text_htPlus2.next_to(vertLine3, DOWN)
        
        self.play(ShowCreation(vertLine3),ShowCreation(text_htPlus2))
        self.play(FadeOut(vertLine2), FadeOut(text_htPlus1))
        self.add(vertLine4)
        self.play(FadeOut(vertLine3), FadeOut(graphGhhtPlusOne),FadeOut(graphLabel3))
        
        text_htMin.next_to(vertLine5,DOWN)
        
        self.play(GrowArrow(arrow))
        self.play(ShowCreation(text_htMin), ShowCreation(vertLine5))
        self.play(FadeOut(text_htPlus2), FadeOut(arrow), FadeOut(vertLine4))
        self.wait(2)
     
    def functionForGraph1(self,x):
        return 2*(x-1.5)*(x-1.5) + 10
     
    def functionForGraph2(self,x):
        return (x+0.5)*(x+0.5)*(x+0.5)*(x+0.5) + 29.44

    def functionForGraph3(self,x):
        return 2*(x-0.5)*(x-0.5)*(x-0.5)*(x-0.5) + 16

class ProofFNPart5_5(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{Auxiliary Function}""")
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)
        textTitle.to_edge(UP)
        
        textFhQuadratic = TexMobject("""\\text{Define an auxiliary function }G(h,h_{t})""")
        textFhQuadratic.next_to(textTitle, DOWN)

        textGhhtLine1 = TexMobject("""G(h,h_{t})=F(h_{t})+(h-h_{t})^{T}\\nabla F(h_{t})""")
        textGhhtLine1.next_to(textFhQuadratic, DOWN)
        textGhhtLine1.set_color(YELLOW)
        textGhhtLine1.scale(0.9)

        textGhhtLine2 = TexMobject("""+\\frac{1}{2}(h-h_{t})^{T}\\left(K(h_{t})\\right)(h-h_{t})""")
        textGhhtLine2.next_to(textGhhtLine1, DOWN)
        textGhhtLine2.set_color(YELLOW)
        textGhhtLine2.scale(0.9)

        textGhhtLine1.shift(LEFT)

        textFhLine1 = TexMobject("""F(h)=F(h_{t})+(h-h_{t})^{T}\\nabla F(h_{t})""")
        textFhLine1.next_to(textGhhtLine2, DOWN)
        textFhLine1.set_color(GREEN)
        textFhLine1.scale(0.9)

        textGhhtLine2.shift(RIGHT)

        textFhLine2 = TexMobject("""+\\frac{1}{2}(h-h_{t})^{T}\\left(W^{T}W\\right)(h-h_{t})""")
        textFhLine2.next_to(textFhLine1, DOWN)
        textFhLine2.set_color(GREEN)
        textFhLine2.shift(RIGHT)
        textFhLine2.scale(0.9)

        textToShowLine1 = TexMobject("\\text{To show: }", "{G(h,h_{t})}", "\\geq", "{F(h)}")
        textToShowLine1.set_color_by_tex_to_color_map({
        "{G(h,h_{t})}": YELLOW,
        "{F(h)}": GREEN     
        })
        textToShowLine1.next_to(textFhLine2, DOWN)
        textToShowLine1.shift(LEFT)

        textFhLine1.shift(LEFT)

        textToShowLine2 = TexMobject(
            "\\Rightarrow", "\\text{To show: }",
            "(h-h_{t})^{T}\\left("
            ,"K(h_{t})",
            "-",
            "W^{T}W",
            "\\right)(h-h_{t})",
            "\\geq",
            "0")
        textToShowLine2.set_color_by_tex_to_color_map({
        "K(h_{t})": YELLOW,
        "W^{T}W": GREEN     
        })
        textToShowLine2.next_to(textToShowLine1, DOWN)

        textAuxGhhtCond1 = TexMobject("""G(h,h_{t})\\geq F(h)""")
        textAuxGhhtCond1.next_to(textToShowLine1, DOWN)
        textAuxGhhtCond1.set_color(YELLOW)

        textAuxGhhtCond2 = TexMobject("""G(h_{t},h_{t})=F(h_{t})""")
        textAuxGhhtCond2.next_to(textAuxGhhtCond1, DOWN)
        textAuxGhhtCond2.set_color(YELLOW)

        self.play(FadeIn(textTitle))
        self.wait(1)
        self.play(FadeIn(textFhQuadratic), FadeIn(textGhhtLine1), FadeIn(textGhhtLine2))
        self.wait(2)
        self.play(FadeIn(textFhLine1), FadeIn(textFhLine2))
        self.play(FadeIn(textToShowLine1))
        self.wait(4.5)
        self.play(FadeIn(textToShowLine2))
        self.wait(2.5)
        self.play(FadeOut(textFhQuadratic),
            FadeOut(textGhhtLine1), FadeOut(textGhhtLine2),
            FadeOut(textFhLine2), FadeOut(textFhLine1),
            FadeOut(textToShowLine1), FadeOut(textToShowLine2))

class ProofFNPart5_6(Scene):


    def construct(self):
        textTitle = TexMobject("""\\text{Auxiliary Function}""")
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)
        textTitle.to_edge(UP)

        textToShowLine1 = TexMobject(
            "\\Rightarrow",
            "\\text{To show: }",
            "(h-h_{t})^{T}\\left("
            ,"K(h_{t})",
            "-",
            "W^{T}W",
            "\\right)(h-h_{t})",
            "\\geq",
            "0")
        textToShowLine1.set_color_by_tex_to_color_map({
        "K(h_{t})": YELLOW,
        "W^{T}W": GREEN     
        })
        textToShowLine1.next_to(textTitle, DOWN)

        textToShowLine2 = TexMobject(
            "\\Rightarrow",
            "\\text{To show: }",
            "K","-","W^{T}W",
            "\\text{ is positive semi-definite.}")
        textToShowLine2.set_color_by_tex_to_color_map({
        "K": YELLOW,
        "W^{T}W": GREEN     
        })
        textToShowLine2.next_to(textToShowLine1, DOWN)

        textMatrixM = TexMobject("""\\text{Consider the matrix, }""")
        textMatrixM.next_to(textToShowLine2,DOWN)

        matrixM = TexMobject("""M=K-W^{T}W=K^{1/2}\\left(I-K^{-1/2}W^{T}WK^{-1/2}\\right)K^{1/2}""")
        matrixM.next_to(textMatrixM,DOWN)
        matrixM.set_color(YELLOW)
        matrixM.shift(0.2*DOWN)

        textMatrixM.shift(3*LEFT+0.2*DOWN)

        textEignenMatrix = TexMobject("""\\text{For matrix }Q=K^{-1/2}W^{T}WK^{-1/2}\\text{,}""")
        textEignenMatrix.next_to(matrixM,DOWN)

        textEignenVec = TexMobject("""\\text{Eigenvector: }
            \\sqrt{\\left(h_{t}\\right)_{i}\\left(W^{T}Wh_{t}\\right)_{i}}
            \\text{ (a positive eignevector)}""")
        textEignenVec.next_to(textEignenMatrix,DOWN)

        textEignenVal = TexMobject("""\\text{Eigenvalue: }1""")
        textEignenVal.next_to(textEignenVec,DOWN)

        textTheoremLine1 = TexMobject("""\\text{Using Frobenius-Perron Theorem, we can show that}""")
        textTheoremLine1.next_to(matrixM, DOWN)

        textTheoremLine2 = TexMobject("""K-W^{T}W\\text{ is positive semi-definite.}""")
        textTheoremLine2.next_to(textTheoremLine1, DOWN)

        textTheoremLine3 = TexMobject("""\\text{Hence, }G(h,h_{t})\\text{ is a valid auxiliary function of }F(h).""")
        textTheoremLine3.next_to(textTheoremLine2, DOWN)
        textTheoremLine3.shift(0.3*DOWN)

        self.add(textTitle)
        self.play(FadeIn(textToShowLine1), FadeIn(textToShowLine2))
        self.play(FadeIn(textMatrixM), FadeIn(matrixM))
        self.wait(2)
        self.play(FadeIn(textEignenMatrix), FadeIn(textEignenVec), FadeIn(textEignenVal))
        self.wait(1)
        self.play(ReplacementTransform(textEignenMatrix, textTheoremLine1),
            ReplacementTransform(textEignenVec, textTheoremLine2),
            ReplacementTransform(textEignenVal, textTheoremLine3))
        self.wait(8)
        self.play(FadeOut(textTitle),
            FadeOut(textToShowLine1), FadeOut(textToShowLine2),
            FadeOut(textMatrixM), FadeOut(matrixM),
            FadeOut(textTheoremLine1), FadeOut(textTheoremLine2), FadeOut(textTheoremLine3))

class ProofFNPart5_7(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{Update Rules - Frobenius Norm}""")
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)
        textTitle.to_edge(UP)

        textFhNonInc = TexMobject("""\\text{So, }F(h)\\text{ is non-increasing under the update rule}""")
        textFhNonInc.next_to(textTitle, 2*DOWN)

        textUpdateh = TexMobject("""h_{t+1}=\\underset{h}{\\textrm{arg min }}G(h,h_{t})""")
        textUpdateh.next_to(textFhNonInc, DOWN)
        textUpdateh.set_color(YELLOW)

        textGradient = TexMobject("""\\text{Taking gradient of }G(h,h_{t})\\text{ and setting to zero,}""")
        textGradient.next_to(textUpdateh, DOWN)
        
        textWRuleElementWise = TexMobject("""W_{ia}\\leftarrow W_{ia}\\frac{\\left(VH^{T}\\right)_{ia}}{\\left(WHH^{T}\\right)_{ia}}""")
        textWRuleElementWise.next_to(textGradient, DOWN)
        textWRuleElementWise.set_color(YELLOW)

        textSimilarly = TexMobject("""\\text{Similarly,}""")
        textSimilarly.next_to(textWRuleElementWise, DOWN)
        textSimilarly.shift(3*LEFT)

        textHRuleElementWise = TexMobject("""H_{au}\\leftarrow H_{au}\\frac{\\left(W^{T}V\\right)_{au}}{\\left(W^{T}WH\\right)_{au}}""")
        textHRuleElementWise.next_to(textSimilarly, DOWN)
        textHRuleElementWise.set_color(YELLOW)
        textHRuleElementWise.shift(3*RIGHT)

        self.play(FadeIn(textTitle))
        self.play(FadeIn(textFhNonInc), FadeIn(textUpdateh))
        self.wait(0.8)
        self.play(FadeIn(textGradient),FadeIn(textWRuleElementWise))
        self.play(FadeIn(textSimilarly), FadeIn(textHRuleElementWise))
        self.wait(2)

        textRuleInMatrixForm = TexMobject("""\\text{Update rules for Frobenius norm in matrix form,}""")
        textRuleInMatrixForm.next_to(textUpdateh, DOWN)

        textWRuleMatrixForm = TexMobject("""W\\leftarrow W\\circ\\frac{VH^{T}}{(WH)H^{T}}""")
        textWRuleMatrixForm.next_to(textRuleInMatrixForm, DOWN)
        textWRuleMatrixForm.set_color(YELLOW)

        textHRuleMatrixForm = TexMobject("""H\\leftarrow H\\circ\\frac{W^{T}V}{{W}^{T}(WH)}""")
        textHRuleMatrixForm.next_to(textWRuleMatrixForm, DOWN)
        textHRuleMatrixForm.set_color(YELLOW)

        textWhere = TexMobject("""\\text{where }/\\text{ and }\\circ\\text{ are elementwise division and multiplication.}""")
        textWhere.next_to(textHRuleMatrixForm,DOWN)
        textWhere.shift(0.2*DOWN)

        self.play(FadeOut(textSimilarly),
            ReplacementTransform(textGradient, textRuleInMatrixForm),
            ReplacementTransform(textWRuleElementWise, textWRuleMatrixForm),
            ReplacementTransform(textHRuleElementWise, textHRuleMatrixForm),
            FadeIn(textWhere))
        self.wait(2)

class ProofFNPart5_8(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{Update Rules - Generalized KLD}""")
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)
        textTitle.to_edge(UP)

        textNewAux = TexMobject("""\\text{Similarly defining a suitable auxiliary function }G(h,h_{t})\\text{,}""")
        textNewAux.next_to(textTitle, 2*DOWN)

        textRuleForKLD = TexMobject("""\\text{the update rules for Generalized KL Divergence are,}""")
        textRuleForKLD.next_to(textNewAux, DOWN)

        
        textWRuleMatrixForm = TexMobject("""W\\leftarrow{W}\\circ\\frac{\\left(\\frac{V}{WH}\\right)H^{T}}{\\mathbf{1}H^{T}}""")
        textWRuleMatrixForm.next_to(textRuleForKLD, DOWN)
        textWRuleMatrixForm.set_color(YELLOW)
        textWRuleMatrixForm.shift(0.2*DOWN)


        textHRuleMatrixForm = TexMobject("""H\\leftarrow H\\circ\\frac{W^{T}\\left(\\frac{V}{WH}\\right)}{W^{T}\\mathbf{1}}""")
        textHRuleMatrixForm.next_to(textWRuleMatrixForm, DOWN)
        textHRuleMatrixForm.set_color(YELLOW)

        textWhereLine1 = TexMobject("""\\text{where }\\mathbf{1}\\text{ is all ones matrix}""")
        textWhereLine1.next_to(textHRuleMatrixForm, DOWN)
        textWhereLine1.shift(0.2*DOWN)

        textWhereLine2 = TexMobject("""/\\text{ and }\\circ\\text{ are elementwise division and multiplication.}""")
        textWhereLine2.next_to(textWhereLine1,DOWN)

        self.play(FadeIn(textTitle))
        self.play(FadeIn(textNewAux))
        self.wait(1.3)
        self.play(FadeIn(textRuleForKLD))
        self.wait(3.5)
        self.play(FadeIn(textWRuleMatrixForm), FadeIn(textHRuleMatrixForm),
            FadeIn(textWhereLine2), FadeIn(textWhereLine1))
        self.wait(5)

#_______ Proposed Algorithm ________

class MonomialMatrixPart1(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{Non-Uniqueness of NMF}""")
        textTitle.to_edge(UP)
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)

        textMathTrivial = TexMobject("""\\text{Trivial: }\\quad{V=WH=IV=VI}""")
        textMathTrivial.next_to(textTitle, DOWN)
        textMathTrivial.shift(DOWN)

        matrixNonUniqueWH = TexMobject("""
        V=WH=WQQ^{-1}H=\\left(WQ\\right)\\left(Q^{-1}H\\right)
        """)
        matrixNonUniqueWH.set_color(YELLOW)
        matrixNonUniqueWH.next_to(textMathTrivial,DOWN)
        matrixNonUniqueWH.shift(DOWN)

        textMonomialQLine1 = TexMobject("""\\text{Not an issue if }Q\\text{ is monomial}""")
        textMonomialQLine1.next_to(matrixNonUniqueWH,DOWN)
        textMonomialQLine1.shift(DOWN)

        textMonomialQLine2 = TexMobject("""\\text{Monomial matrix: a permuted diagonal matrix}""")
        textMonomialQLine2.next_to(textMonomialQLine1,DOWN)

        self.play(FadeIn(textTitle))
        self.wait(1)
        self.play(Write(textMathTrivial))
        self.wait(1)
        self.play(Write(matrixNonUniqueWH))
        self.wait(3)
        self.play(FadeIn(textMonomialQLine1))
        self.play(FadeIn(textMonomialQLine2))
        self.wait(2)

class MonomialMatrixPart2(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{Non-Uniqueness - Monomial Matrix }Q""")
        textTitle.to_edge(UP)
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)

        matrixMath = TexMobject("""
        V
        =
        \\left[
            \\begin{array}{ccc}
                {W}_{11} & \\hdots & {W}_{1r}  \\\\
                \\vdots & \\hdots & \\hdots   \\\\
                \\vdots & \\hdots & \\hdots   \\\\
                {W}_{m1} & \\hdots & {W}_{mr}
            \\end{array}
        \\right]
        \\left[
            \\begin{array}{cccc}
                {H}_{11} & \\hdots & \\hdots & {H}_{n1} \\\\
                \\vdots & \\hdots & \\hdots & \\hdots  \\\\
                {H}_{1r} & \\hdots & \\hdots & {H}_{rn}
            \\end{array}
        \\right]
        """)
        matrixMath.set_color(YELLOW)
        matrixMath.scale(0.8)
        matrixMath.next_to(textTitle,DOWN)
        matrixMath.shift(0.5*DOWN)

        textMath = TexMobject("""{V=WH}""")
        textMath.set_color(YELLOW)
        textMath.move_to(textTitle.get_corner(DOWN)+DOWN)

        self.play(FadeIn(textTitle), FadeIn(textMath))
        self.play(Transform(textMath, matrixMath))
        self.play(ApplyMethod(textMath.copy().move_to, textTitle.get_corner(DOWN)+5*DOWN))

class MonomialMatrixPart3(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{Non-Uniqueness - Monomial Matrix }Q""")
        textTitle.to_edge(UP)
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)

        matrixMath = TexMobject("""
        V
        =
        \\left[
            \\begin{array}{ccc}
                {W}_{11} & \\hdots & {W}_{1r}  \\\\
                \\vdots & \\hdots & \\hdots   \\\\
                \\vdots & \\hdots & \\hdots   \\\\
                {W}_{m1} & \\hdots & {W}_{mr}
            \\end{array}
        \\right]
        \\left[
            \\begin{array}{cccc}
                {H}_{11} & \\hdots & \\hdots & {H}_{n1} \\\\
                \\vdots & \\hdots & \\hdots & \\hdots  \\\\
                {H}_{1r} & \\hdots & \\hdots & {H}_{rn}
            \\end{array}
        \\right]
        """)
        matrixMath.set_color(YELLOW)
        matrixMath.scale(0.8)
        matrixMath.next_to(textTitle,DOWN)
        matrixMath.shift(0.5*DOWN)

        matrixMathCopy2 = TexMobject("""
        V
        =
        \\left[
            \\begin{array}{ccc}
                {W}_{11} & \\hdots & {W}_{1r}  \\\\
                \\vdots & \\hdots & \\hdots   \\\\
                \\vdots & \\hdots & \\hdots   \\\\
                {W}_{m1} & \\hdots & {W}_{mr}
            \\end{array}
        \\right]
        \\left[
            \\begin{array}{cccc}
                {H}_{11} & \\hdots & \\hdots & {H}_{n1} \\\\
                \\vdots & \\hdots & \\hdots & \\hdots  \\\\
                {H}_{1r} & \\hdots & \\hdots & {H}_{rn}
            \\end{array}
        \\right]
        """)
        matrixMathCopy2.set_color(YELLOW)
        matrixMathCopy2.scale(0.8)
        matrixMathCopy2.move_to(textTitle.get_corner(DOWN)+5*DOWN)

        self.add(textTitle)
        self.add(matrixMath)
        self.add((matrixMathCopy2))

        matrixMathCopy3 = TexMobject("""
        V
        =
        \\left[
            \\begin{array}{ccc}
                {W}_{1r} & \\hdots & {W}_{11}  \\\\
                \\vdots & \\hdots & \\hdots   \\\\
                \\vdots & \\hdots & \\hdots   \\\\
                {W}_{mr} & \\hdots & {W}_{m1}
            \\end{array}
        \\right]
        \\left[
            \\begin{array}{cccc}
                {H}_{1r} & \\hdots & \\hdots & {H}_{rn} \\\\
                \\vdots & \\hdots & \\hdots & \\hdots  \\\\
                {H}_{11} & \\hdots & \\hdots & {H}_{n1}
            \\end{array}
        \\right]
        """)
        matrixMathCopy3.set_color(YELLOW)
        matrixMathCopy3.scale(0.8)
        matrixMathCopy3.move_to(textTitle.get_corner(DOWN)+5*DOWN)

        pointer1 = CurvedArrow(LEFT+1.5*DOWN,3*LEFT+1.5*DOWN,color=RED)
        pointer2 = CurvedArrow(2*RIGHT+1.5*DOWN,2*RIGHT+2.7*DOWN,color=RED)
        pointer3 = CurvedArrow(3*LEFT+2*DOWN, LEFT+2*DOWN,color=RED)
        pointer4 = CurvedArrow(3*RIGHT+2.7*DOWN, 3*RIGHT+1.5*DOWN,color=RED)

        self.play(FadeOut(matrixMathCopy2), FadeIn(matrixMathCopy3),
            FadeIn(pointer1), FadeIn(pointer2), FadeIn(pointer3), FadeIn(pointer4))
        self.wait(1)

        textForQ = TexMobject("""\\text{In case of monomial matrix }Q\\text{,}
        """)
        textForQ.move_to(textTitle.get_corner(DOWN)+DOWN)

        matrixNonUniqueWH = TexMobject("""
        V=WH=WQQ^{-1}H=\\left(WQ\\right)\\left(Q^{-1}H\\right)
        """)
        matrixNonUniqueWH.set_color(YELLOW)
        matrixNonUniqueWH.scale(0.8)
        matrixNonUniqueWH.next_to(textForQ, DOWN)

        textSwapScale = TexMobject("""
        \\text{It is just swapping and scaling of rows and columns.}
        """)
        textSwapScale.next_to(matrixNonUniqueWH, DOWN)

        self.play(FadeOut(matrixMath),
            FadeIn(textForQ), FadeIn(matrixNonUniqueWH), FadeIn(textSwapScale))
        self.wait(2)

class Priors(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{Priors Imposed on }W\\text{ and }H""")
        textTitle.to_edge(UP)
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)

        textSource = TexMobject("""S_{j}=\\sum_{k=1}^{n} {W(:,k)}\\times{H(k,j)}""")
        textSource.next_to(textTitle,DOWN)
        textSource.shift(0.5*DOWN)
        textSource.set_color(YELLOW)
        textSource.scale(1.2)

        textSourceLHS = TexMobject("""j^{\\text{th}}\\text{ source}=\\sum_{k=1}^{n} \\left({k}^{\\text{th}}\\text{ component}\\right)""")
        textSourceLHS.next_to(textSource,DOWN)
        textSourceLHS.shift(1.9*LEFT)

        textSourceRHS = TexMobject("""\\times\\left(\\text{encoding of }{k}^{\\text{th}}\\text{component}\\right)""")
        textSourceRHS.next_to(textSourceLHS,DOWN)
        textSourceRHS.shift(4.5*RIGHT)

        textHTimeDep = TexMobject("""\\text{Columns of }H\\text{ act as time-dependent encodings,}""")
        textHTimeDep.next_to(textSourceRHS,DOWN)
        textHTimeDep.shift(0.5*DOWN+2.5*LEFT)
        textHTimeDep.set_color(YELLOW)

        textPriorsOnlyOnH = TexMobject("""\\text{so these priors are applied only on }H.""")
        textPriorsOnlyOnH.next_to(textHTimeDep,DOWN)
        textPriorsOnlyOnH.set_color(YELLOW)

        self.play(FadeIn(textTitle))
        self.wait(3)
        self.play(FadeIn(textSource),
            FadeIn(textSourceLHS), FadeIn(textSourceRHS),
            FadeIn(textHTimeDep))
        self.wait(3)
        self.play(FadeIn(textPriorsOnlyOnH))
        self.wait(1)
        self.play(FadeOut(textSource),
            FadeOut(textSourceLHS), FadeOut(textSourceRHS),
            FadeOut(textHTimeDep), FadeOut(textPriorsOnlyOnH))

class TemporalContinuity(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{Priors Imposed on }W\\text{ and }H""")
        textTitle.to_edge(UP)
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)

        textTempCont = TexMobject("""\\text{Temporal Continuity}""")
        textTempCont.next_to(textTitle,DOWN)
        textTempCont.set_color(YELLOW)
        textTempCont.scale(1.2)
        textTempCont.shift(0.3*DOWN)

        textMathCostFunc = TexMobject("\\text{Cost function: }",
            "{c}_{T}(H)=\\sum_{j=1}^{n}\\left(\\frac{1}{\\sigma_{j}^{2}}\\sum_{t=2}^{r}\\left(h_{t,j}-h_{t+1,j}\\right)^{2}\\right)")
        textMathCostFunc.next_to(textTempCont,DOWN)
        textMathCostFunc.shift(0.3*DOWN)
        textMathCostFunc.set_color_by_tex_to_color_map({
        "Cost function: ": RED
        })

        textMathNorm = TexMobject("\\text{Normalization: }",
            "{\\sigma_{j}=\\sqrt{\\left(1/r\\right)\\sum_{t=1}^{r}h_{t,j}^{2}}")
        textMathNorm.next_to(textMathCostFunc,DOWN)
        textMathNorm.set_color_by_tex_to_color_map({
        "Normalization: ": RED
        })

        textDiffBWFrames = TexMobject("""\\text{Penalizes large differences between the frames }({h}_{t,j}-{h}_{t+1,j})""")
        textDiffBWFrames.next_to(textMathNorm,DOWN)
        textDiffBWFrames.set_color(GREEN)
        textDiffBWFrames.shift(0.2*DOWN)

        self.add(textTitle)
        self.play(FadeIn(textTempCont))
        self.wait(1)
        self.play(Write(textMathCostFunc))
        self.play(Write(textMathNorm))
        self.wait(3)
        self.play(FadeIn(textDiffBWFrames))
        self.wait(2.5)
        self.play(FadeOut(textTempCont),
            FadeOut(textMathCostFunc), FadeOut(textMathNorm),
            FadeOut(textDiffBWFrames))

class Sparsity(Scene):

    def construct(self):
        textTitle = TexMobject("""\\text{Priors Imposed on }W\\text{ and }H""")
        textTitle.to_edge(UP)
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)

        textSparsness = TexMobject("""\\text{Sparseness}""")
        textSparsness.next_to(textTitle,DOWN)
        textSparsness.set_color(YELLOW)
        textSparsness.scale(1.2)
        textSparsness.shift(0.3*DOWN)

        textMathCostFunc = TexMobject("\\text{Cost function: }",
            "c_{S}(H)=\\sum_{j=1}^{n}\\sum_{t=1}^{r}\\left|h_{j,t}/\\sigma_{j}\\right|")
        textMathCostFunc.next_to(textSparsness,DOWN)
        textMathCostFunc.shift(0.3*DOWN)
        textMathCostFunc.set_color_by_tex_to_color_map({
        "Cost function: ": RED
        })

        textMathNorm = TexMobject("\\text{Normalization: }",
            "{\\sigma_{j}=\\sqrt{\\left(1/r\\right)\\sum_{t=1}^{r}h_{t,j}^{2}}")
        textMathNorm.next_to(textMathCostFunc,DOWN)
        textMathNorm.set_color_by_tex_to_color_map({
        "Normalization: ": RED
        })

        textSparsenessMessage = TexMobject("""\\text{Expresses overlapping spectra as sum and residue}""")
        textSparsenessMessage.next_to(textMathNorm,DOWN)
        textSparsenessMessage.set_color(GREEN)
        textSparsenessMessage.shift(0.2*DOWN)

        self.add(textTitle)
        self.play(FadeIn(textSparsness))
        self.wait(1)
        self.play(Write(textMathCostFunc))
        self.play(Write(textMathNorm))
        self.wait(3)
        self.play(FadeIn(textSparsenessMessage))
        self.wait(2.5)

        self.play(FadeOut(textTitle), FadeOut(textSparsness),
            FadeOut(textMathCostFunc), FadeOut(textMathNorm),
            FadeOut(textSparsenessMessage))

class TotalCost(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{Total Cost Function}""")
        textTitle.to_edge(UP)
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)

        textSum = TexMobject("""\\text{Weighted sum of three terms: }""")
        textSum.next_to(textTitle,DOWN)
        textSum.set_color(YELLOW)
        textSum.scale(1.2)
        textSum.shift(0.5*DOWN)

        textCostKLD = TexMobject("\\text{Reconstruction error: }D\\left(V||WH\\right)")
        textCostKLD.next_to(textSum,DOWN)
        textCostKLD.shift(0.5*DOWN)

        textCostTemp = TexMobject("\\text{Temporal continuity: }{c}_{T}(H)")
        textCostTemp.next_to(textCostKLD,DOWN)

        textCostSparse = TexMobject("\\text{Sparsity: }c_{S}(H)")
        textCostSparse.next_to(textCostTemp,DOWN)

        textTotalCost = TexMobject("""c\\left(W,H\\right)=D\\left(V||WH\\right)+\\alpha{c}_{T}\\left(H\\right)+\\beta{c}_{S}\\left(H\\right)""")
        textTotalCost.next_to(textCostSparse,DOWN)
        textTotalCost.set_color(YELLOW)
        textTotalCost.shift(0.5*DOWN)

        textModifiedUpdateRules = TextMobject("""\\text{Update rules modified for this cost function.}""")
        textModifiedUpdateRules.next_to(textTotalCost,DOWN)
        textModifiedUpdateRules.set_color(GREEN)

        self.add(textTitle)
        self.play(FadeIn(textSum),
            FadeIn(textCostKLD), FadeIn(textCostTemp), FadeIn(textCostSparse),
            Write(textTotalCost))
        self.wait(0.5)
        self.play(FadeIn(textModifiedUpdateRules))
        self.wait(2.5)

class UpdateRulesFinal1(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{Final Update Rules}""")
        textTitle.to_edge(UP)
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)

        textMessage = TexMobject("""\\text{Considering all the three cost functions,}""")
        textMessage.next_to(textTitle,DOWN)
        textMessage.shift(0.2*DOWN)

        textCostFunc = TexMobject("""c\\left(W,H\\right)=D\\left(V||WH\\right)+\\alpha{c}_{T}\\left(H\\right)+\\beta{c}_{S}\\left(H\\right)""")
        textCostFunc.next_to(textMessage,DOWN)

        textWRule = TexMobject("""W\\leftarrow\\frac{W\\circ\\left(\\frac{V}{WH}\\right)H^{T}}{\\mathbf{1}H^{T}}""")
        textWRule.next_to(textCostFunc, DOWN)
        textWRule.shift(DOWN)
        textWRule.set_color(YELLOW)

        textWRuleExplLine1 = TexMobject("""\\text{where }\\mathbf{1}\\text{ is all ones matrix}""")
        textWRuleExplLine1.next_to(textWRule, DOWN)
        textWRuleExplLine1.shift(0.5*DOWN)

        textWRuleExplLine2 = TexMobject("""/\\text{ and }\\circ\\text{ are elementwise division and multiplication.}""")
        textWRuleExplLine2.next_to(textWRuleExplLine1,DOWN)

        self.play(FadeIn(textTitle), FadeIn(textMessage), FadeIn(textCostFunc),
            FadeIn(textWRule), FadeIn(textWRuleExplLine1), FadeIn(textWRuleExplLine2))
        self.wait(1)

class UpdateRulesFinal2(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{Final Update Rules}""")
        textTitle.to_edge(UP)
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)

        textGrad1_rPlus = TexMobject("""\\nabla c_{r}^{+} (\\textbf{W, H}) = \\textbf{W}^\\textbf{T}\\textbf{1}""")
        textGrad1_rPlus.next_to(textTitle,DOWN)
        textGrad1_rPlus.set_color(YELLOW)
        textGrad1_rPlus.shift(0.5*DOWN)

        textGrad2_rMinus = TexMobject("""\\nabla c_{r}^{-} (\\textbf{W, H}) = \\textbf{W}^\\textbf{T}\\frac{\\textbf{V}}{\\textbf{WH}} """)
        textGrad2_rMinus.next_to(textGrad1_rPlus, DOWN)
        textGrad2_rMinus.set_color(YELLOW)

        textGrad3_tPlus = TexMobject("""[\\nabla c_{t}^{+} (\\textbf{H})]_{j,t} = \\frac{4Th_{j,t}}{\\sum_{i=1}^{T} h^{2}_{j,i} } """)
        textGrad3_tPlus.next_to(textGrad2_rMinus, DOWN)
        textGrad3_tPlus.set_color(YELLOW)

        textGrad4_tMinus = TexMobject("""[\\nabla c_{t}^{-} (\\textbf{H})]_{j,t} = 2T\\frac{h_{j,t-1}+h_{j,t+1}}{\\sum_{i=1}^{T} h^{2}_{j,i}} + \\frac{2Th_{j,t}\\sum_{i=2}^{T} (h_{j,i}-h_{j,i-1})^2}{\\sum_{i=1}^{T} h^{2}_{j,i} }""")
        textGrad4_tMinus.next_to(textGrad3_tPlus,DOWN)
        textGrad4_tMinus.to_edge(LEFT)
        textGrad4_tMinus.set_color(YELLOW)

        textGrad5_sPlus = TexMobject("""[\\nabla c_{s}^{+} (\\textbf{H})]_{j,t} = \\frac{1}{\\sqrt{\\frac{1}{T}\\sum_{i=1}^{T} h^{2}_{j,i}} }   """)
        textGrad5_sPlus.next_to(textTitle,DOWN)
        textGrad5_sPlus.shift(0.3*DOWN)
        textGrad5_sPlus.set_color(YELLOW)
        textGrad5_sPlus.to_edge(RIGHT)

        textGrad6_sMinus = TexMobject("""[\\nabla c_{s}^{-} (\\textbf{H})]_{j,t} =\\frac{h_{j,t}\\sqrt{T}\\sum_{i=1}^{T} h_{j,i}}{\\left(\\sum_{i=1}^{T} h^{2}_{j,i}\\right)^2 } """)
        textGrad6_sMinus.next_to(textGrad5_sPlus,DOWN)
        textGrad6_sMinus.set_color(YELLOW)
        textGrad6_sMinus.to_edge(RIGHT)

        textGrad1_rPlus.to_edge(LEFT)
        textGrad2_rMinus.to_edge(LEFT)
        textGrad3_tPlus.to_edge(LEFT)

        scaleFactor = 0.8
        textGrad1_rPlus.scale(scaleFactor)
        textGrad2_rMinus.scale(scaleFactor)
        textGrad3_tPlus.scale(scaleFactor)
        textGrad4_tMinus.scale(scaleFactor)
        textGrad5_sPlus.scale(scaleFactor)
        textGrad6_sMinus.scale(scaleFactor)

        textExplLine = TexMobject("""\\text{where }/\\text{ and }\\circ\\text{ are elementwise division and multiplication.}""")
        textExplLine.to_edge(DOWN)

        self.play(FadeIn(textTitle),
            FadeIn(textGrad1_rPlus), FadeIn(textGrad2_rMinus),
            FadeIn(textGrad3_tPlus), FadeIn(textGrad4_tMinus),
            FadeIn(textGrad5_sPlus), FadeIn(textGrad6_sMinus),
            FadeIn(textExplLine))
        self.wait(1)

class UpdateRulesFinal3(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{Final Update Rules}""")
        textTitle.to_edge(UP)
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)

        textHRule = TexMobject("""H\\leftarrow H\\circ\\frac{\\nabla c^{-}_{r}(W,H)+\\nabla c^{-}_{t}(W,H)+\\nabla c^{-}_{s}(W,H)}{\\nabla c^{+}_{r}(W,H)+\\nabla c^{+}_{t}(W,H)+\\nabla c^{+}_{s}(W,H)}""")
        textHRule.next_to(textTitle, 3*DOWN)
        textHRule.set_color(YELLOW)
        textHRule.shift(0.5*DOWN)

        textHRuleExplLine = TexMobject("""\\text{where }/\\text{ and }\\circ\\text{ are elementwise division and multiplication.}""")
        textHRuleExplLine.next_to(textHRule,2*DOWN)

        self.play(FadeIn(textTitle), FadeIn(textHRule), FadeIn(textHRuleExplLine))
        self.wait(1)

class ImplementedAlgorithm(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{Algorithm""")
        textTitle.to_edge(UP)
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)

        textStep1 = TexMobject("""\\text{1. Initialize }W\\text{ and }H\\text{ with absolute Gaussian noise.}""")
        textStep1.next_to(textTitle,DOWN)
        textStep1.shift(DOWN)

        textStep2 = TexMobject("""\\text{2. Update W.}""")
        textStep2.next_to(textStep1,2*DOWN)
        
        textStep3 = TexMobject("""\\text{3. Update H.}""")
        textStep3.next_to(textStep2,2*DOWN)

        textStep4 = TexMobject("""\\text{4. Iterate until cost function converges.}""")
        textStep4.next_to(textStep3,2*DOWN)

        textStep1.to_edge(LEFT)
        textStep1.shift(RIGHT)

        textStep2.to_edge(LEFT)
        textStep2.shift(RIGHT)

        textStep3.to_edge(LEFT)
        textStep3.shift(RIGHT)

        textStep4.to_edge(LEFT)
        textStep4.shift(RIGHT)

        self.play(FadeIn(textTitle))
        self.play(FadeIn(textStep1),FadeIn(textStep2), FadeIn(textStep3), FadeIn(textStep4))
        self.wait(2)

#_______ Simulation ________

class SimulationOuterProdcuct(Scene):
	def construct(self):
		textTitle = TexMobject("""\\text{Obtaining Sources from }W\\text{ and }H""")
		textTitle.to_edge(UP)
		textTitle.set_color(BLUE)
		textTitle.scale(1.5)

		textWH = TexMobject("""W\\text{ and }H\\text{ obtained using update rules}""")
		textWH.next_to(textTitle,DOWN)
		textWH.shift(0.5*DOWN)

		textOuterProduct = TexMobject("""\\text{Magnitude Spectra of }{i}^{\\text{th}}\\text{ source}
			=W(:,i)\\otimes{H(i,:)}""")
		textOuterProduct.next_to(textWH,DOWN)
		textOuterProduct.set_color(YELLOW)
		textOuterProduct.shift(DOWN)

		textMagSpectra = TexMobject("""\\text{Magnitude Spectra  }\\circ""")
		textMagSpectra.next_to(textOuterProduct,DOWN)
		textMagSpectra.shift(DOWN)

		textEqualTo = TexMobject("""=""")
		textEqualTo.next_to(textOuterProduct,DOWN)
		textEqualTo.shift(DOWN)

		textMagSpectra.shift(3*LEFT)
		textEqualTo.shift(3*RIGHT)

		self.play(FadeIn(textTitle))
		self.play(FadeIn(textWH))
		self.wait(4)
		self.play(FadeIn(textOuterProduct))
		self.wait(5)
		self.play(FadeIn(textMagSpectra), FadeIn(textEqualTo))
		self.wait(4)

class SimulationSNR(Scene):
    def construct(self):
        textTitle = TexMobject("""\\text{SNR of Proposed Algorithm}""")
        textTitle.to_edge(UP)
        textTitle.set_color(BLUE)
        textTitle.scale(1.5)

        textSNR = TexMobject("""\\text{SNR}(m,j) = \\frac{\\sum\\nolimits_{k,t} [Y_m]^{2}_{k,t}}{\\sum\\nolimits_{k,t} ([Y_m]_{k,t}- [\\hat{Y_j}]_{k,t})^2""")
        textSNR.next_to(textTitle,DOWN)
        textSNR.shift(0.3*DOWN)
        textSNR.set_color(YELLOW)

        textWhereLine1 = TexMobject("""Y_{m} = \\text{magnitude spectrogram of the }m^{th}\\text{ reference}""")
        textWhereLine1.next_to(textSNR,2*DOWN)
        
        textWhereLine2 = TexMobject("""\\hat{Y_j}\\text{ = magnitude spectrogram of the }j^{th}\\text{ separated component}""")
        textWhereLine2.next_to(textWhereLine1,2*DOWN)

        textHighestSNR = TexMobject("""\\text{We use }m=j\\text{ which gives the highest SNR}""")
        textHighestSNR.next_to(textWhereLine2,2.1*DOWN)

        textProposedAlgo = TexMobject("""\\text{Proposed algorithm had the highest SNR.}""")
        textProposedAlgo.next_to(textHighestSNR,2*DOWN)
        textProposedAlgo.set_color(YELLOW)

        textWhereLine1.to_edge(LEFT)
        textWhereLine1.shift(0.1*RIGHT)

        textWhereLine2.to_edge(LEFT)
        textWhereLine2.shift(0.1*RIGHT)

        self.play(FadeIn(textTitle))
        self.wait(2)
        self.play(FadeIn(textSNR))
        self.play(FadeIn(textWhereLine1), FadeIn(textWhereLine2), FadeIn(textHighestSNR))
        self.wait(4.5)
        self.play(FadeIn(textProposedAlgo))
        self.wait(3)
