import random as r
import tkinter as tk
from PIL import ImageTk, Image

country = {"Flags/ad.png": "Andorra",
           "Flags/ae.png": "United Arab Emirates",
           "Flags/af.png": "Afghanistan",
           "Flags/ag.png": "Antigua and Barbuda",
           "Flags/ai.png": "Anguilla",
           "Flags/al.png": "Albania",
           "Flags/am.png": "Armenia",
           "Flags/ao.png": "Angola",
           "Flags/ar.png": "Argentina",
           "Flags/at.png": "Austria",
           "Flags/au.png": "Australia",
           "Flags/aw.png": "Aruba",
           "Flags/az.png": "Azerbaijan",
           "Flags/ba.png": "Bosnia and Herzegovina",
           "Flags/bb.png": "Barbados",
           "Flags/bd.png": "Bangladesh",
           "Flags/be.png": "Belgium",
           "Flags/bf.png": "Burkina Faso",
           "Flags/bg.png": "Bulgaria",
           "Flags/bh.png": "Bahrain",
           "Flags/bi.png": "Burundi",
           "Flags/bj.png": "Benin",
           "Flags/bm.png": "Bermuda",
           "Flags/bn.png": "Brunei",
           "Flags/bo.png": "Bolivia",
           "Flags/br.png": "Brazil",
           "Flags/bs.png": "Bahamas",
           "Flags/bt.png": "Bhutan",
           "Flags/no.png": "Norway",
           "Flags/bw.png": "Botswona",
           "Flags/by.png": "Belarus",
           "Flags/bz.png": "Belize",
           "Flags/ca.png": "Canada",
           "Flags/cd.png": "Democratic Republic of Congo",
           "Flags/cf.png": "Central African Republic",
           "Flags/cg.png": "Republic of the Congo",
           "Flags/ch.png": "Switzerland",
           "Flags/ci.png": "Ivory Coast",
           "Flags/cl.png": "chile",
           "Flags/cm.png": "Cameroon",
           "Flags/cn.png": "China",
           "Flags/co.png": "Colombia",
           "Flags/cr.png": "Costa Rica",
           "Flags/cu.png": "Cuba",
           "Flags/cv.png": "Cape Verde",
           "Flags/cw.png": "Curacao",
           "Flags/cy.png": "Cyprus",
           "Flags/cz.png": "Czech republic",
           "Flags/de.png": "Germany",
           "Flags/dj.png": "Dijbouti",
           "Flags/dk.png": "Denmark",
           "Flags/dm.png": "Dominica",
           "Flags/do.png": "Dominican Republic",
           "Flags/dz.png": "Algeria",
           "Flags/ec.png": "Ecuador",
           "Flags/ee.png": "Estonia",
           "Flags/eg.png": "Egypt",
           "Flags/eh.png": "Western Sahara",
           "Flags/er.png": "Eritrea",
           "Flags/es.png": "Spain",
           "Flags/et.png": "Ethiopia",
           "Flags/fi.png": "Finland",
           "Flags/fj.png": "Fiji",
           "Flags/fm.png": "Micronesia",
           "Flags/fr.png": "France",
           "Flags/ga.png": "Gabon",
           "Flags/gb.png": "United Kingdom",
           "Flags/gb-eng.png": "England",
           "Flags/gb-nir.png": "Northern Ireland",
           "Flags/gb-sct.png": "Scotland",
           "Flags/gb-wls.png": "Wales",
           "Flags/gd.png": "Grenada",
           "Flags/ge.png": "Georgia",
           "Flags/gh.png": "Ghana",
           "Flags/gl.png": "Greenland",
           "Flags/gm.png": "Gambia",
           "Flags/gn.png": "Guinea",
           "Flags/gr.png": "Greece",
           "Flags/gt.png": "Guatemala",
           "Flags/gw.png": "Guinea Bissau",
           "Flags/gy.png": "Guyana",
           "Flags/hk.png": "Hong Kong",
           "Flags/hn.png": "Honduras",
           "Flags/hr.png": "Croatia",
           "Flags/ht.png": "Haiti",
           "Flags/hu.png": "Hungary",
           "Flags/id.png": "Indonesia",
           "Flags/ie.png": "Ireland",
           "Flags/il.png": "Israel",
           "Flags/in.png": "India",
           "Flags/iq.png": "Iraq",
           "Flags/ir.png": "Iran",
           "Flags/is.png": "Iceland",
           "Flags/it.png": "Italy",
           "Flags/jm.png": "Jamacia",
           "Flags/jo.png": "Jordan",
           "Flags/jp.png": "Japan",
           "Flags/ke.png": "Kenya",
           "Flags/kg.png": "Kyrgyzstan",
           "Flags/ki.png": "Kiribati",
           "Flags/km.png": "Comoros",
           "Flags/kn.png": "St Kitts and Nevis",
           "Flags/kp.png": "North Korea",
           "Flags/kr.png": "South Korea",
           "Flags/kw.png": "Kuwait",
           "Flags/ky.png": "Cayman Islands",
           "Flags/kz.png": "Kazakhstan",
           "Flags/la.png": "Laos",
           "Flags/lb.png": "Lebanon",
           "Flags/lc.png": "St Lucia",
           "Flags/li.png": "Liechtenstein",
           "Flags/lk.png": "Sri Lanka",
           "Flags/lr.png": "Liberia",
           "Flags/ls.png": "Lesotho",
           "Flags/lt.png": "Lithuania",
           "Flags/lu.png": "Luxembourg",
           "Flags/lv.png": "Latvia",
           "Flags/ly.png": "Libya",
           "Flags/ma.png": "Morocco",
           "Flags/mc.png": "Monaco",
           "Flags/md.png": "Moldova",
           "Flags/me.png": "Montenegro",
           "Flags/mg.png": "Madagascar",
           "Flags/mh.png": "Marshall Islands",
           "Flags/mk.png": "North Macedonia",
           "Flags/ml.png": "Mali",
           "Flags/mm.png": "Myanmar",
           "Flags/mn.png": "Mongolia",
           "Flags/mr.png": "Mauritania",
           "Flags/mt.png": "Malta",
           "Flags/mu.png": "Mauritius",
           "Flags/mv.png": "Maldives",
           "Flags/mw.png": "Malawi",
           "Flags/mx.png": "Mexico",
           "Flags/my.png": "Malaysia",
           "Flags/mz.png": "Mozambique",
           "Flags/na.png": "Namibia",
           "Flags/ne.png": "Niger",
           "Flags/ng.png": "Nigeria",
           "Flags/ni.png": "Nicaragua",
           "Flags/nl.png": "Netherlands",
           "Flags/np.png": "Nepal",
           "Flags/nz.png": "New Zealand",
           "Flags/om.png": "Oman",
           "Flags/pa.png": "Panama",
           "Flags/pe.png": "Peru",
           "Flags/pg.png": "Papa New Guinea",
           "Flags/ph.png": "Philippines",
           "Flags/pk.png": "Pakistan",
           "Flags/pl.png": "Poland",
           "Flags/pr.png": "Puerto Rico",
           "Flags/ps.png": "Palestine",
           "Flags/pt.png": "Portugal",
           "Flags/pw.png": "Palau",
           "Flags/py.png": "Paraguay",
           "Flags/qa.png": "Qatar",
           "Flags/ro.png": "Romania",
           "Flags/rs.png": "Serbia",
           "Flags/ru.png": "Russia",
           "Flags/rw.png": "Rwanda",
           "Flags/sa.png": "Saudi Arabia",
           "Flags/sb.png": "Solomon Islands",
           "Flags/sd.png": "Sudan",
           "Flags/se.png": "Sweden",
           "Flags/sg.png": "Singapore",
           "Flags/si.png": "Slovenia",
           "Flags/sk.png": "Slovakia",
           "Flags/sl.png": "Sierra Leone",
           "Flags/sm.png": "San Marino",
           "Flags/sn.png": "Senegal",
           "Flags/so.png": "Somalia",
           "Flags/sr.png": "Suriname",
           "Flags/ss.png": "South Sudan",
           "Flags/st.png": "Sao Tome and Principe",
           "Flags/sv.png": "El Salvador",
           "Flags/sx.png": "Sint Maarten",
           "Flags/sy.png": "Syria",
           "Flags/sz.png": "Eswatini",
           "Flags/tc.png": "Turks and Caicos Islands",
           "Flags/td.png": "Chad",
           "Flags/tg.png": "Togo",
           "Flags/th.png": "Thailand",
           "Flags/tj.png": "Tajikistan",
           "Flags/tl.png": "Timor-Leste",
           "Flags/tm.png": "Turkmenistan",
           "Flags/tn.png": "Tunisia",
           "Flags/to.png": "Tonga",
           "Flags/tr.png": "Turkey",
           "Flags/tt.png": "Trinidad and Tobago",
           "Flags/tv.png": "Tuvalu",
           "Flags/tw.png": "Taiwan",
           "Flags/tz.png": "Tanzania",
           "Flags/ua.png": "Ukraine",
           "Flags/ug.png": "Uganda",
           "Flags/us.png": "United States of America",
           "Flags/uy.png": "Uruguay",
           "Flags/uz.png": "Uzbekistan",
           "Flags/va.png": "Vatican City",
           "Flags/vc.png": "Saint Vincent and the Grenadines",
           "Flags/ve.png": "Venezuela",
           "Flags/vn.png": "Vietnam",
           "Flags/vu.png": "Vanuatu",
           "Flags/ws.png": "Samoa",
           "Flags/xk.png": "Kosovo",
           "Flags/ye.png": "Yemen",
           "Flags/za.png": "South Africa",
           "Flags/zm.png": "Zambia",
           "Flags/zw.png": "Zimbabwe"}

print(input("Welcome to guess the flag! \n\n"
            ""
            "The rules are simple: \n\n"
            ""
            "A flag will be randomly generated and your job is to guess it. \n\n"
            ""
            "You have 3 tries to guess each flag.\n\n"
            ""
            "You can choose between two options:\n"
            "1- Use the hint, therefore, For every letter that you guess correctly it will print it in its position.\n"
            "2- Test your actual abilities and do not use the hint.\n\n"
            ""
            "Remember write the countries in full length and no capitalization is needed.\n\n"
            ""
            "Please press enter to start playing: "))


def random_flag():
    flag = r.choice(list(country.keys()))
    return flag


def open_image(flag):
    close = tk.Tk()
    flag_image = ImageTk.PhotoImage(Image.open(flag))
    label = tk.Label(close, image=flag_image).pack()
    close.after(1250, lambda: close.destroy())
    close.mainloop()


def flag_hint(temp, answer):
    s = []

    len_answer = (len(answer))
    for z in range(0, len_answer):
        s.append("_")

    for j in temp:
        if j in answer:
            for l in range(len_answer):
                if answer[l] == j:
                    s[l] = j

    s2 = ''.join(s)
    print(s2)


def enable_disable(hint, temp, answer):
    if hint == "yes":
        print(flag_hint(temp, answer))
    else:
        print("")


hint = input("Do you want to have hints? enter yes, if not press enter. ")
print(hint)


def flag_game(count):
    rdm_flag = random_flag()
    open_image(rdm_flag)
    answer = country[rdm_flag].lower()
    temp = input("Guess the country using the flag: \n")
    i = 0
    count = count

    while i < 2 and answer != temp:

        if temp == "skip":
            pass
            break
        enable_disable(hint, temp, answer)
        temp = input("Try again: \n")
        i += 1

    if answer == temp:
        print("You have guessed the flag!")
        count += 1
        print("You have guessed", count, "out of", 15, "flags! \n")  # correct it

    else:
        print("Better luck next time, the answer was: ", answer)
        print("You have guessed", count, "out of", 15, "flags! \n")

    return count


def game_loop():
    x = 0
    z = 14
    c = flag_game(0)
    while x < z:
        c = flag_game(c)
        x += 1


game_loop()
