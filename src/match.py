from pypinyin import pinyin, Style
import re, json

def match_by_option(mode, hetero, target):
    with open('./data/lib.json') as f:
        lib = json.load(f, encoding='utf-8')
    if mode == '-e':
        return match_exact(lib, target)
    elif mode == '-t':
        return match_tone(lib, target, hetero)
    elif mode == '-v':
        return match_vague(lib, target, hetero)


def match_exact(lib, target):
    assert(len(target) == 1)
    results = []
    for w in lib:
        if w['init'] == target:
            results += w['idioms']
    return results


def match_tone(lib, target, hetero):
    if len(target) == 1:
        tone = pinyin(target, heteronym=hetero, style=Style.TONE3)[0]
    elif re.match('[a-zA-Z]+[1-4]', target):
        tone = [target]
    else:
        raise Exception
    check_list = 'tone' if not hetero else 'tone_hetero'
    results = []
    for w in lib:
        if check_consistency(tone, w[check_list]):
            results += w['idioms']
    return results


def match_vague(lib, target, hetero):
    if len(target) == 1:
        tone_vague = pinyin(target, heteronym=hetero, style=Style.NORMAL)[0]
    elif re.match('[a-zA-Z]+', target):
        tone_vague = [target]
    else:
        raise Exception
    results = []
    check_list = 'vague' if not hetero else 'vague_hetero'
    for w in lib:
        if check_consistency(tone_vague, w[check_list]):
            results += w['idioms']
    return results


def check_consistency(tone_target, tone_word):
    return any([t in tone_word for t in tone_target])