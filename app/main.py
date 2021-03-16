import streamlit as st
import numpy as np
import cv2
from PIL import Image, ImageEnhance

OUTPUT_WIDTH = 500


def main():
    st.title("MasterClass-Aula")
    st.text("Carlos Matheus - Aula MasterClass")
    st.sidebar.title("Menu Options")

    #####################
    #     MenuOption    #
    #####################

    menu_option = ["Filtros","Sobre"]
    escolha     = st.sidebar.selectbox("Options", menu_option)

    #####################
    # Upload da imagem  #
    #####################
    if escolha == "Filtros":
        our_image = Image.open("./placeholder.png")
        # st.image(our_image)
        extensoes = ['jpg', 'png', 'jpeg']
        image_file = st.file_uploader("Coloque sua imagem", type=extensoes)
        if image_file is not None:
            our_image = Image.open(image_file)
            st.text("Look it´s you !!!")
            st.sidebar.text("Imagem Original")
            st.sidebar.image(our_image, width=150)

            #####################
            # Filtro aplocaveis #
            #####################

        filtros = st.sidebar.radio("Filtros", ['Original', 'GrayScale', 'Desenho', 'Serpia', 'Contraste', 'Blur', 'Canny'])

  


        if filtros == 'Original':
            converted_img = np.array(our_image.convert('RGB'))
            st.image(converted_img, width=OUTPUT_WIDTH)

        elif filtros == 'GrayScale':
            converted_img = np.array(our_image.convert('RGB'))
            gray_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
            st.image(gray_img, width=OUTPUT_WIDTH)

        elif filtros == 'Desenho':
            b_amount = st.sidebar.slider("Kernel (n, n)", 3, 81, 9, step=2)
            converted_img = np.array(our_image.convert('RGB'))
            gray_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
            inv_gray_image = 255 - gray_img
            blur_image = cv2.GaussianBlur(inv_gray_image, (b_amount, b_amount), 0, 0)
            sketch_image = cv2.divide(gray_img, 255 - blur_image, scale=256)
            st.image(sketch_image, width=OUTPUT_WIDTH)

        elif filtros == 'Serpia':
            converted_img = np.array(our_image.convert('RGB'))
            gray_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2BGR)
            serpia = [
                [0.272, 0.534, 0.131],
                [0.346, 0.686, 0.168],
                [0.393, 0.769, 0.189]
            ]
            kernel = np.array(serpia)
            serpia_img = cv2.filter2D(converted_img, -1, kernel)
            serpia = cv2.cvtColor(serpia_img, cv2.COLOR_BGR2RGB)
            st.image(serpia, channels="BGR", width=OUTPUT_WIDTH)

        elif filtros == 'Blur':
            b_amount = st.sidebar.slider("Kernel (n, n)", 3, 81, 9, step=2)
            converted_img = np.array(our_image.convert('RGB'))
            gray_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2BGR)
            blur_image = cv2.GaussianBlur(converted_img, (b_amount, b_amount), 0, 0)
            st.image(blur_image, width=OUTPUT_WIDTH)


        elif filtros == 'Canny':
            b_amount = st.sidebar.slider("Kernel (n, n)", 3, 81, 9, step=2)
            converted_img = np.array(our_image.convert('RGB'))
            converted_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2BGR)
            blur = cv2.GaussianBlur(converted_img, (b_amount, b_amount), 0)
            canny = cv2.Canny(blur, 100, 150)
            st.image(canny, width=OUTPUT_WIDTH)

        elif filtros == 'Contraste':
            c_amount = st.sidebar.slider("Contraste", 0.0, 2.0, 1.0)
            contraste = ImageEnhance.Contrast(our_image)
            contraste_img = contraste.enhance(c_amount)
            st.image(contraste_img, width=OUTPUT_WIDTH)

        else:
            st.image(our_image, width=OUTPUT_WIDTH)

    elif escolha == "Sobre":
        st.subheader("Projeto 1 da masterclass Visão Computacional, do Sigmoidal")
        st.markdown("Para mais informações, entre em [o site do Sigmoidal](http://sigmoidal.ai)")
        st.text("Aluno Carlos Matheus ")
        st.markdown("Github -> [git](https://github.com/DuplamenteH)")



if __name__ == '__main__':
    main()
