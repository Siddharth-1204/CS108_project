awk -F',' '
{
    # remove Windows carriage return safely
    sub(/\r$/, "", $0)

    # skip malformed or empty rows early
    if (NF < 6) next

   

    player1 = $1
    player2 = $2
    winner = $3
    game = $6

    # skip invalid entries
    if (winner == "" || game == "" || player1 == "" || player2 == "") next
    
    # skip tie cases
    if (winner != "tie") {
        loser = (winner == player1 ? player2 : player1)

        wins[winner, game]++
        losses[loser, game]++
    # array of all player and game pairs
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
} | column -t -s ','