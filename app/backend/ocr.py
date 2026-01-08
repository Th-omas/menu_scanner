from paddleocr import PaddleOCR

ocr_model = PaddleOCR(lang="chinese_cht")

def run_ocr(image_path):
    result = ocr_model.predict(image_path)
    print(result)
    lines = []
    for line in result:
        lines.append(line[1][0])
    return lines
