import matplotlib
from matplotlib import font_manager, rc
import platform

def korean():
    try :
        if platform.system() == 'Windows':
            font_name = font_manager.FontProperties\
                (fname="c:/windows/Fonts/malgun.ttf").get_name()
            rc('font', family=font_name)
        else:
            # Mac
            rc('font', family='AppleGothic')
    except:
        pass

    matplotlib.rcParams['axes.unicode_minus'] = False