from genericpath import exists
import os
import cv2
import imutils

def video_2_images(video_path:str, output_image_folder:str, min_frame:int = 1, max_frame:int = 0, visible:bool = False):

    if not os.path.isdir(output_image_folder):
        print('The output image folder does not exist')
        exit()
    
    if not os.path.exists(os.path.join(os.getcwd(), video_path)) or video_path.split('.')[-1] != 'mp4':
        print('The input video folder does not exist or the file is not in mp4 format!')
        exit()
    
    video_name = (video_path.split('/')[-1]).split('.')[0]
    
    video_Capture = cv2.VideoCapture(video_path)
    if video_Capture is None or not video_Capture.isOpened():
        print('Unable to open the video')
        exit()
    
    print("[INFO] video capturing started...")

    video_frames = int(video_Capture.get(cv2.CAP_PROP_FRAME_COUNT))
    max_frame = max_frame if 0 < max_frame <= video_frames else video_frames
    min_frame = min_frame if min_frame >= 1 else 1

    counter = 0
    while (video_Capture.isOpened()):
        counter += 1
        ret, frame = video_Capture.read()
        if ret:
            if min_frame <= counter <= max_frame:
                image_path = os.path.join(output_image_folder,video_name+"_Frame_"+str(counter)+'.png')
                cv2.imwrite(image_path,frame)

                if visible:  
                    # frame = imutils.resize(frame,width=740)
                    cv2.startWindowThread()
                    cv2.imshow(video_name,frame)            
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            elif counter > max_frame and visible:
                if cv2.waitKey() & 0xFF == ord('q'):
                    break
            elif counter > max_frame:
                break

        else:
            break
    video_Capture.release()
    # cv2.distoryAllWindows()


def display_video(video_path:str, min_frame:int = 1, max_frame:int = 0):

    if not os.path.exists(os.path.join(os.getcwd(), video_path)) or video_path.split('.')[-1] != 'mp4':
        print('The input video folder does not exist or the file is not in mp4 format!')
        exit()
    
    video_name = (video_path.split('/')[-1]).split('.')[0]
    
    video_Capture = cv2.VideoCapture(video_path)
    if video_Capture is None or not video_Capture.isOpened():
        print('Unable to open the video')
        exit()
    
    print("[INFO] video capturing started...")

    video_frames = int(video_Capture.get(cv2.CAP_PROP_FRAME_COUNT))
    max_frame = max_frame if 0 < max_frame <= video_frames else video_frames
    min_frame = min_frame if min_frame >= 1 else 1

    counter = 0
    while (video_Capture.isOpened()):
        counter += 1
        ret, frame = video_Capture.read()
        if ret:
            if min_frame <= counter <= max_frame:
                frame = imutils.resize(frame,width=740)
                cv2.startWindowThread()
                cv2.imshow(video_name,frame)            
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        else:
            break
    video_Capture.release()
    # cv2.distoryAllWindows()

def save_video_mp4(video_path:str, 
                    min_frame:int = 1,
                    max_frame:int = 0,
                    output_path:str=None,
                    output_name:str='Output',
                    new_width:int = 1280,
                    new_height:int = 720):
    if output_path == None:
        print('Please provide an output path for the video!')
        exit()

    if not os.path.exists(os.path.join(os.getcwd(), video_path)) or video_path.split('.')[-1] != 'mp4':
        print('The input video folder does not exist or the file is not in mp4 format!')
        exit()

    video_name = (video_path.split('/')[-1]).split('.')[0]
    
    video_Capture = cv2.VideoCapture(video_path)
    if video_Capture is None or not video_Capture.isOpened():
        print('Unable to open the video')
        exit()
    
    # fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    # output_video_name = output_name + '.avi'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video_name = output_name + '.mp4'

    print(output_video_name)
    output_video_path = os.path.join(output_path,output_video_name)
    print(output_video_path)
    # self._cap = VideoCapture(0)
    
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (new_width,new_height))
    
    print("[INFO] video capturing started...")

    video_frames = int(video_Capture.get(cv2.CAP_PROP_FRAME_COUNT))
    max_frame = max_frame if 0 < max_frame <= video_frames else video_frames
    min_frame = min_frame if min_frame >= 1 else 1

    counter = 0
    while (video_Capture.isOpened()):
        counter += 1
        ret, frame = video_Capture.read()
        if ret:
            if min_frame <= counter <= max_frame:
                frame = imutils.resize(frame,width=new_width,height=new_height)
                out.write(frame)
                
                cv2.startWindowThread()
                cv2.imshow(video_name,frame)            
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        else:
            break
    video_Capture.release()
    out.release()
    # cv2.distoryAllWindows()


video_path = "C:/Users/ssoltani/OneDrive - ArcelorMittal/Desktop/POC_Crop_Shear/Yolo3_Keras/keras-yolo3/output/CropShearBox_uuid-1f8112bc-417c-4cf4-828c-d9434ca0b8fd_2021-11-16_00-00-00(1).mp4"
output_image_folder = "C:/Users/ssoltani/OneDrive - ArcelorMittal/Desktop/POC_Crop_Shear/1st_try/Data/output_image_temp"
output_video_path = "C:/Users/ssoltani/OneDrive - ArcelorMittal/Desktop/"
# video_2_images(video_path,output_image_folder, visible=False)
# display_video(video_path=video_path)
save_video_mp4(video_path,output_path=output_video_path,output_name='test2')