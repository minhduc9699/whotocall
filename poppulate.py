from models.name import *
from gtts import gTTS
import mlab

list_char = ["Lớp trưởng",
             "Lớp phó",
             "Bí thư"",
             "Phó bí thư",
             "Quản ca",
             "Bạn nam cao nhất lớp",
             "Bạn nữ cao nhất lớp',
             "Bạn nam thấp nhất lớp',
             "Bạn nữ thấp nhất lớp',
             "Bạn nam mập nhất lớp',
             "Bạn nữ mập nhất lớp",
             "Bạn nam còi nhất lớp",
             "Bạn nữ còi nhất lớp",
             "Học sinh trong đội bóng đá của lớp",
             "Học sinh trong đội văn nghệ của lớp",
             "Học sinh ngồi gần cửa ra vào",
             "Học sinh ngồi góc lớp",
             "Học sinh ngồi bàn đầu",
             "Học sinh ngồi bàn cuối",
             "Học sinh ở cuối danh sách lớp",
             "Học sinh ở đầu danh sách lớp"
]

list_state = [
            "Học sinh đầu tiên nhìn vào mắt bạn",
            "Học sinh đang nói chuyện riêng",
            "Học sinh nữ có kiểu tóc đặc biệt",
            "Học sinh nam có kiểu tóc đặc biệt",
            "Học sinh có màu áo giống bạn",
            "Học sinh có sinh nhật trong tuần này",
            'Học sinh có tên giống bạn',
            "Học sinh hay đi học muộn",
            "Học sinh hay ăn quà vặt",
            "Học sinh hay ngủ gật",
            "Học sinh là con út",
            "Học sinh là con một",
            "Học sinh là con một",
            "Học sinh có phụ huynh là bác sĩ",
            "Học sinh có phụ huynh là công an",
            "Học sinh có phụ huynh là giáo viên",
            "Học sinh có tên dài nhất lớp"
]

list_audio = [
            "anh chị nào đang nhìn tôi"
            'anh chị nào đang nói chuyện riêng'
            'anh nào có kiểu tóc dị nhất'
            'chị nào có kiểu tóc điệu nhất'
            'anh chị nào mặc màu áo giống tôi'
            'anh chị nào có sinh nhật trong tuần này'
            'anh chị nào tên giống tôi'
            'anh chị nào hay đi muộn'
            'anh chị nào hay ăn quà vặt'
            'anh chị nào hay ngủ gật'
            'anh chị nào là con út'
            'anh chị nào là con một'
            'anh chị nào là con cả'
            'anh chị nào có bố mẹ là bác sĩ'
            'anh chị nào có bố mẹ là công an'
            'anh chị nào có bố mẹ là giáo viên'
            'anh chị nào gọi tên cũng phát mệt'


]

new_audio =


new_char = Option(char=list_char, state=list_state)
