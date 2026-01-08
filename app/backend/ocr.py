from paddleocr import PaddleOCR

ocr_model = PaddleOCR(lang="chinese_cht")

def run_ocr(image_path):
    result = ocr_model.predict(image_path)
    return result[0]["rec_texts"]


def analyze_vlm(image_path):
    return "toto"