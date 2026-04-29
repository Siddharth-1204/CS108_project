echo "Enter username of player1 :"
read name1

echo "Enter password :"
read -s pass1
Hashpass1=$(echo -n "${pass1}" | sha256sum | awk '{print $1}')

userline1=$(grep "^${name1}," users.csv)

input="nothing"

while [[ -z "$userline1" ]]; do
    echo "User doesn't exist want to retry or register (ry/rg)"
    read input

    while [[ "$input" != "rg" && "$input" != "ry" ]]; do
        echo "Give valid input ry for retry, rg for register"
        read input
    done

    if [[ "$input" == "rg" ]]; then
        break
    fi

    echo "Again enter username of player1 :"
    read name1
    userline1=$(grep "^${name1}," users.csv)
done

if [[ "$input" == "rg" ]]; then
    echo "Enter password :"
    read -s pass1
    Hashpass1=$(echo -n "${pass1}" | sha256sum | awk '{print $1}')
    echo "${name1},${Hashpass1}" >> users.csv
    userline1="${name1},${Hashpass1}"
else
    try=3
    while [[ "$userline1" != "${name1},${Hashpass1}" && $try -gt 1 ]]; do
        echo "Password is incorrect, try again"
        echo "Enter password again:"
        read -s pass1
        Hashpass1=$(echo -n "${pass1}" | sha256sum | awk '{print $1}')
        try=$((try-1))
    done

    if [[ "$userline1" != "${name1},${Hashpass1}" ]]; then
        echo "Password is incorrect"
        echo "Sorry! You used your 3 tries"
        exit 1
    fi
fi

# ---------------- PLAYER 2 ----------------

echo "Enter username of player2 :"
read name2

echo "Enter password :"
read -s pass2
Hashpass2=$(echo -n "${pass2}" | sha256sum | awk '{print $1}')

userline2=$(grep "^${name2}," users.csv)

input="nothing"

while [[ -z "$userline2" ]]; do
    echo "User doesn't exist want to retry or register (ry/rg)"
    read input

    while [[ "$input" != "rg" && "$input" != "ry" ]]; do
        echo "Give valid input ry for retry, rg for register"
        read input
    done

    if [[ "$input" == "rg" ]]; then
        break
    fi

    echo "Again enter username of player2 :"
    read name2
    userline2=$(grep "^${name2}," users.csv)
done

if [[ "$input" == "rg" ]]; then
    echo "Enter password :"
    read -s pass2
    Hashpass2=$(echo -n "${pass2}" | sha256sum | awk '{print $1}')
    echo "${name2},${Hashpass2}" >> users.csv
    userline2="${name2},${Hashpass2}"
else
    try=3
    while [[ "$userline2" != "${name2},${Hashpass2}" && $try -gt 1 ]]; do
        echo "Password is incorrect, try again"
        echo "Enter password again:"
        read -s pass2
        Hashpass2=$(echo -n "${pass2}" | sha256sum | awk '{print $1}')
        try=$((try-1))
    done

    if [[ "$userline2" != "${name2},${Hashpass2}" ]]; then
        echo "Password is incorrect"
        echo "Sorry! You used your 3 tries"
        exit 1
    fi
fi

# ---------------- START GAME ----------------

python3 game.py "$name1" "$name2"
