import fitz

document = fitz.open("Nontapat_Auetrongjit_CV.pdf")
page = document[2]
pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
pixmap.save("tmp/braincode_cv_page.png")
