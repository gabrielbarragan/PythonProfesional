def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "solo puedes usar strings"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("hola"))

    repeat_3 = make_repeater_of(3)
    print(repeat_3("Gabriel"))

if '__main__' == __name__:
    run()