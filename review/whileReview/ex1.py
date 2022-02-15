while True:
    st = input('input nmber')

    if st == 'q':
        break
    if st.isalpha():
        print('retry1')
        continue
    elif not (st.isalpha()) and not (st.isnumeric()):
        print('retry2...')
        continue
    else:
        num = int(st)
        print(num * 100)