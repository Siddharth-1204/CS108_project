awk -F',' '
{
    # remove Windows carriage return safely
    sub(/\r$/, "", $0)

    # skip malformed or empty rows early
    if (NF < 6) next

    # trim whitespace from all fields
    for (i = 1; i <= NF; i++) {
        gsub(/^[ \t]+|[ \t]+$/, "", $i)
    }

    p1 = $1
    p2 = $2
    winner = $3
    game = $6

    # skip invalid entries
    if (winner == "" || game == "" || p1 == "" || p2 == "") next

    if (winner != "tie") {
        loser = (winner == p1 ? p2 : p1)

        wins[winner, game]++
        losses[loser, game]++

        players[winner, game] = 1
        players[loser, game] = 1
    }
}
END {
    print "Player,Game,Wins,Losses,Ratio"

    for (key in players) {
        split(key, arr, SUBSEP)
        player = arr[1]
        game = arr[2]

        w = wins[player, game] + 0
        l = losses[player, game] + 0

        ratio = (l == 0 ? "-" : sprintf("%.2f", w/l))

        print player "," game "," w "," l "," ratio
    }
}
' history.csv |
{
    read header
    echo "$header"

    case "$1" in
        wins)
            sort -t',' -k3,3nr
            ;;
        losses)
            sort -t',' -k4,4nr
            ;;
        ratio)
            sort -t',' -k5,5nr
            ;;
        *)
            sort -t',' -k3,3nr
            ;;
    esac
}