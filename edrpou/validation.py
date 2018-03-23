def valid8(code):
    weights = list(range(1, 8))
    if 30000000 < int(code) < 60000000:
        weights = [weights[-1]] + weights[:-1]
    check_sum = sum([weights[i] * int(c) for i, c in enumerate(code[:7])])
    if check_sum % 11 == 10:
        check_sum = sum([(weights[i] + 2) * int(c) for i, c in enumerate(code[:7])])
    if str(check_sum % 11)[-1] == code[-1]:
        return True
    return False


def valid10(code):
    weights = [-1, 5, 7, 9, 4, 6, 10, 5, 7]
    check_sum = sum([weights[i] * int(c) for i, c in enumerate(code[:9])])
    if str(check_sum % 11)[-1] == code[-1]:
        return True
    return False


def valid(code):
    work_code = str(code).strip()
    if work_code.isnumeric():
        work_code = str(int(work_code))
        if len(work_code) <= 8:
            work_code = work_code.zfill(8)
        else:
            work_code = work_code.zfill(10)
        if len(work_code) == 8:
            return valid8(work_code), work_code
        if len(work_code) == 10:
            return valid10(work_code), work_code
    return False, work_code


if __name__ == '__main__':
    print(valid('23086311'))
    # print(valid('30000000'))
    # print(valid('60000000'))
    print(valid('12345678'))
    print(valid('31080212'))
    print(valid('32428230'))
    print(valid('32459549'))
    print(valid('39391794'))
    print(valid('32884569'))

    print(valid('2833808134'))
    print(valid('39605280'))
    print(valid('34493190'))
    print(valid('24420280'))
    print(valid('25196910'))
    print(valid('06714960'))
    print(valid('32952570'))
    print(valid('41606880'))
    print(valid('31038700'))
    print(valid('25875060'))
    print(valid('40317990'))

    print(valid('20250169'))
    print(valid('37981596'))
    print(valid('31207551'))
    print(valid('38173906'))
    print(valid('24828718'))
    print(valid('38747742'))
    print(valid('30649239'))
    print(valid('30362029'))
    print(valid('39059453'))
    print(valid('22779582'))
    print(valid('12130048'))
    print(valid('12365478'))
    print(valid('12110074'))
    print(valid('12070061'))
    print(valid('00000006'))
    print(valid('02300187'))
    print(valid('02300193'))
    print(valid('31080212'))
    print(valid('18581593'))
    print(valid('12148153'))
    print(valid('12090076'))
    print(valid('19345551'))
    print(valid('12148062'))
    print(valid('00000007'))
    print(valid('02300056'))
    print(valid('00000011'))
    print(valid('12148118'))
    print(valid('12092462'))
    print(valid('12148116'))
    print(valid('12148144'))
    print(valid('13101700'))
    print(valid('02300007'))
    print(valid('18581639'))
    print(valid('51100102'))
    print(valid('12090060'))
    print(valid('13393384'))
    print(valid('12100055'))
    print(valid('31952588'))
    print(valid('00000019'))
    print(valid('00790187'))
    print(valid('02300186'))
    print(valid('12148170'))
    print(valid('00000001'))
    print(valid('12140376'))
    print(valid('32428230'))
    print(valid('12148141'))
    print(valid('00000009'))
    print(valid('02300207'))
    print(valid('02300778'))
    print(valid('12148229'))
    print(valid('12148115'))
    print(valid('12140310'))
    print(valid('02300209'))
    print(valid('23588815'))
    print(valid('12148228'))
    print(valid('12100053'))
    print(valid('20941127'))
    print(valid('32459549'))
    print(valid('22050039'))
    print(valid('02300184'))
    print(valid('24523304'))
    print(valid('26036625'))
    print(valid('39391794'))
    print(valid('13893456'))
    print(valid('02300202'))
    print(valid('20854575'))
    print(valid('00324976'))
    print(valid('01732552'))
    print(valid('22079826'))
    print(valid('22116825'))
    print(valid('21027786'))
    print(valid('02300196'))
    print(valid('00000014'))
    print(valid('32884569'))
    print(valid('13710184'))
    print(valid('00000013'))
    print(valid('00000008'))
    print(valid('23086311'))
    print(valid('12148143'))
    print(valid('00000010'))
    print(valid('25499941'))
    print(valid('12148147'))
    print(valid('12110109'))
    print(valid('02300922'))
    print(valid('03357189'))
    print(valid('14258516'))
    print(valid('36287657'))
    print(valid('03770391'))
    print(valid('02300006'))
