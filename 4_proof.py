from big_ol_pile_of_manim_imports import *

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
