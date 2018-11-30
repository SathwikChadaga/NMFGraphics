from big_ol_pile_of_manim_imports import *

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
