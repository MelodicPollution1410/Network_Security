import subprocess

# Function to get the number of devices connected in a network
def capture(ip):
    command = 'sudo nmap -v '+ip+'/24'
    #print(command)
    command = command.split()

    cmd = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = cmd.stdout.read().decode()
    count = 0
    x = (output)
    text_file = open("sample.txt", "wt")
    n = text_file.write(x)
    text_file.close()
    file = 'sample.txt'
    out = []
    out1 = []
    with open(file, 'r') as fp:
        lines = fp.readlines()
        for i in lines:
            if ('172' in i):
                out.append(i)
        for x in out:
            split_results = x.split('for ')
            out1.append(split_results[1])
    numb = str(len(out1))
    #print('Number of devices in the network: '+ numb)
    #print('Device details: ')
    dev = [s.strip('\n') for s in out1]
    #for i in dev:
       # print(i)
    return numb,dev

#ip="172.39.3.7"
#capture(ip)