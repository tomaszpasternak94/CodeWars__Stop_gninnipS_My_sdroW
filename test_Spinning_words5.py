import Stop_gninnipS_My_sdroW

def test_spin():
    assert Stop_gninnipS_My_sdroW.spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
    assert Stop_gninnipS_My_sdroW.spin_words("This is a test") == "This is a test"
    assert Stop_gninnipS_My_sdroW.spin_words("This is another test") == "This is rehtona test"

def test_spinWithNumbers():
    assert Stop_gninnipS_My_sdroW.spin_words('100 donuts') == '100 stunod'
    assert Stop_gninnipS_My_sdroW.spin_words('10000 donuts') == '00001 stunod'

def test_spinOneWordWithSpace():
    assert Stop_gninnipS_My_sdroW.spin_words('P Y T H O N') == 'P Y T H O N'

def test_spinSpaceWordSpace():
    assert Stop_gninnipS_My_sdroW.spin_words(' empty ') == ' ytpme '
