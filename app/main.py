from altair.vegalite.v4.schema import channels
import streamlit as st
import numpy as np
import cv2
from PIL import Image, ImageEnhance

OUTPUT_WIDTH = 500
global img_convert

def Fill(filtros, our_image):
    
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
            b_amount = st.sidebar.slider("Kernel (n, n)", 3, 81, 9, step=3)
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


def filter_video(camera,filter,run=True):
    count=0
            
    FRAME = st.image([])
    slider =st.slider("Intensidade : Filtros Desenho até Canny", 3, 81, 9, step=2)
    while run :
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if filter == 'Original':
            count += 1
            img = Image.fromarray(frame)
            img_convert = img.convert("RGB")
            convert = np.array(img_convert)
            #converted_img = np.array(frame.convert('RGB'))
            FRAME.image(convert)

        elif filter == 'GrayScale':
            count += 1
            img = Image.fromarray(frame)
            img_convert = img.convert("RGB")
            convert = np.array(img_convert)
            cinza = cv2.cvtColor(convert,cv2.COLOR_RGB2GRAY)
            FRAME.image(cinza)

        elif filter == 'Desenho':
            b_amount = slider
            img = Image.fromarray(frame)
            convert_img = img.convert("RGB")
            converted_img = np.array(convert_img)
            gray_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
            inv_gray_image = 255 - gray_img
            blur_image = cv2.GaussianBlur(inv_gray_image, (b_amount, b_amount), 0, 0)
            sketch_image = cv2.divide(gray_img, 255 - blur_image, scale=256)
            FRAME.image(sketch_image)

        elif filter == 'Serpia':
            img = Image.fromarray(frame)
            convert_img = img.convert("RGB")
            converted_img = np.array(convert_img)
            gray_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2BGR)
            serpia_f = [
                [0.272, 0.534, 0.131],
                [0.346, 0.686, 0.168],
                [0.393, 0.769, 0.189]
            ]
            norm_slider = slider/100
            serpia = np.array(serpia_f)
            f = np.dot(serpia,norm_slider)
            kernel = np.array(f)
            serpia_img = cv2.filter2D(converted_img, -1, kernel)
            serpia = cv2.cvtColor(serpia_img, cv2.COLOR_BGR2RGB)
            #st.image(serpia, channels="BGR", width=OUTPUT_WIDTH)
            FRAME.image(serpia,channels="BGR")

        elif filter == 'Blur':
            count += 1
            #b_amount =st.number_input(label='15',min_value=3,max_value=81)
            #converted_img = np.array(frame.convert('RGB'))
            #gray_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2BGR)
            img = Image.fromarray(frame)
            img_convert = img.convert("RGB")
            convert = np.array(img_convert)
            #cinza = cv2.cvtColor(convert,cv2.COLOR_RGB2GRAY)
            blur_image = cv2.GaussianBlur(convert, (slider, slider), 0, 0)
            #st.image(blur_image, width=OUTPUT_WIDTH)
            FRAME.image(blur_image)


        elif filter == 'Canny':
            #count += 1
            b_amount = slider
            img = Image.fromarray(frame)
            img_convert = img.convert("RGB")
            convert = np.array(img_convert)
            blur = cv2.GaussianBlur(convert, (b_amount, b_amount), 0)
            canny = cv2.Canny(blur, 100, 150)
            FRAME.image(canny)
            

        elif filter == 'Contraste':
            
           
            #if keyboard.is_pressed('+'):  
            #    count += 1
            #    print('+1 {}'.format(count))
            #if ke




            c_amount = slider
            img = Image.fromarray(frame)
            img_convert = img.convert("RGB")
            contraste = ImageEnhance.Contrast(img_convert)
            contraste_img = contraste.enhance(c_amount)
            FRAME.image(contraste_img)
            count += 1

        else:
            FRAME.image(frame)
        count += 1


def main():
    st.title("MasterClass-Aula")
    st.text("Carlos Matheus - Aula MasterClass")
    st.sidebar.title("Menu Options")

    #####################
    #     MenuOption    #
    #####################

    menu_option = ["Filtros","Sobre"]
    escolha     = st.sidebar.selectbox("Options", menu_option)


    menu_cam = ["camera","foto"]
    op = st.selectbox("Camera ou foto",menu_cam)


    #####################
    # Upload da imagem  #
    #####################
    

    if escolha == "Filtros":
        if op=="foto":
            our_image = Image.open("app/placeholder.png")
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
            Fill(filtros,our_image)
        else:

            st.text("Para alternar para video marque abaixo")
            run = st.checkbox('Run')
            FRAME_WINDOW = st.image([])
            camera = cv2.VideoCapture(0)

            filtros = st.sidebar.radio("Filtros", ['Original', 'GrayScale', 'Desenho', 'Serpia', 'Contraste', 'Blur', 'Canny'])
            filter_video(camera,filtros,run)






        







    elif escolha == "Sobre":
        st.subheader("Projeto 1 da masterclass Visão Computacional, do Sigmoidal")
        st.markdown("Para mais informações, entre em [o site do Sigmoidal](http://sigmoidal.ai)")
        st.text("Aluno Carlos Matheus ")
        st.markdown("Github -> [git](https://github.com/DuplamenteH)")



if __name__ == '__main__':
    main()
