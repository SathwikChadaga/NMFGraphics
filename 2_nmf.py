from big_ol_pile_of_manim_imports import *

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
