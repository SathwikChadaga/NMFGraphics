from big_ol_pile_of_manim_imports import *

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

