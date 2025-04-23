import cv2
import matplotlib.pyplot as plt
import easyocr

def recognize_text(img_path):
    '''Loads an image and recognizes text.'''
    reader = easyocr.Reader(['en'])  # For English
    return reader.readtext(img_path)

def overlay_ocr_text(img_path, save_name="output_overlay"):
    '''Loads an image, recognizes text, and overlays it.'''
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    dpi = 80
    fig_width, fig_height = int(img.shape[0] / dpi), int(img.shape[1] / dpi)
    plt.figure()
    f, axarr = plt.subplots(1, 2, figsize=(fig_width, fig_height))
    axarr[0].imshow(img)

    result = recognize_text(img_path)

    for (bbox, text, prob) in result:
        if prob >= 0.2:
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = (int(top_left[0]), int(top_left[1]))
            bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

            cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 2)
            cv2.putText(img, text, (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    axarr[1].imshow(img)
    plt.savefig(f"{save_name}.jpg", bbox_inches='tight')

def ocr_text(img_path):
    '''Extracts text and counts words.'''
    result = recognize_text(img_path)
    op = ""
    count = 0
    for (bbox, text, prob) in result:
        if prob:
            count += len(text.split(" "))
            op += "\n" + text
    return op, count
