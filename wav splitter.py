a="""00:00:00;Intro
00:00:32;A few words from Bertel
00:03:04;Michael introduces the first 3 pieces
00:04:36;Heyr, himna smithur — Porkell Sigurbjörnsson (1938-2013) 
00:07:28;Vivo Ego, dicit Dominus — Alonso Lobo (1555-1617)
00:10:09;Tebe Poem — P.I. Tchaikovski (1840-1893)
00:11:59;Marion introduces the next 3 pieces
00:13:25;Denn er hat seinen Engeln befohlen über dir—Elias — Mendelssohn-Bartholdy (1809-1847)
00:16:52;Hebe deine Augen auf—Elias — Mendelssohn-Bartholdy (1809-1847) — (Anna, Marion, Susanna)
00:18:32;Coventry Carol — Arranged by Martin Shaw
00:21:00;Bertel introduces the next 3 pieces
00:23:33;Moh Oshiv (Psalm 116) — Remi Studer (1983) — (Men)
00:26:22;A Dieu ma voix (Psalm 77) — Jan Sweelinck (1562-1612)
00:29:09;Hans Hassler (1564-1612) — Ach weh des Leiden (D'Octa)
00:31:33;David introduces the next 3 pieces
00:33:39;Den Tod niemand zwingen kunnt — J.S. Bach BWV4 (1685-1750) — (David and Kate)
00:38:27;Verhoort heer myn geclach (Psalm 5) — Jacobus Clemens non Papa (1510-1565) — (Kate, David, Bertel)
00:40:05;Chantez a Dieu (Psalm 96) (D'Octa) — Jan Sweelinck (1562-1621) 
00:41:51;Pierre introduces the next 2 pieces
00:43:10;Nunc Dimittis — Josquin des Prez (1440-1521)
00:48:36;Agni Pathene (O Virgin Pure) — St. Nectarios (late 19th Century) — (David, Bertel, Pierre)
00:53:07;Emma introduces the next 2 pieces; the Nordic block
00:54:50;Ave Generosa — Ola Gjeilo (1978) — (Women)
00:59:25;Frid pa Jord (Peace on Earth) — Olivia Blyberg, Sofia Karlsson — (Emma, Kate, Susanna, David, Bertel)
01:02:10;Kate introduces the next 2 pieces
01:03:34;Stille Nacht, Heilige Nacht (Silent Night) — Franz Gruber (1787-1863)
01:06:27;Riu, Rui, Chiu — Mateo Flecha the Elder (1481-1553)
01:08:30;End"""

from pydub import AudioSegment
import datetime

def secondsAndTitleFrom2timestamps(string1,string2):
    timestampStr1, title = string1.split(";")
    timestampStr2, _ = string2.split(";")
    dt1 = datetime.datetime.strptime("2000-01-01 "+timestampStr1, "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.datetime.strptime("2000-01-01 "+timestampStr2, "%Y-%m-%d %H:%M:%S")
    s = (dt2 - dt1).seconds
    print(s, title)
    return s, title
    
 
lastMs = 0
for i in range(len(a.splitlines())-1):
    string1 = a.splitlines()[i]
    string2 = a.splitlines()[i+1]
    s, title = secondsAndTitleFrom2timestamps(string1,string2)
    
    t1 = lastMs #Works in milliseconds
    t2 = lastMs + s * 1000
    lastMs = t2
    newAudio = AudioSegment.from_wav("C:\Chittering Chamber Choir Dec 2023.wav")
    newAudio = newAudio[t1:t2]
    newAudio.export(f"C:\Chittering Wavs\{i+1}. {title}.wav", format="wav")