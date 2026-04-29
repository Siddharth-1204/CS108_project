awk '
BEGIN{
    FS = ",";
}
{
    wins_player_game[$1 "," $4]++
    losses_player_game[$2 "," $4]++
    player[$1,$4]=1
    player[$2,$4]=1
}
END{
    print "Player, Game, Wins, Losses, Ratio"
    for ( string in player ){
        split(string,arr,",")

        game = arr[2]
        gamer = arr[1]
        key = gamer,game

        wins = wins_player_game[key] + 0
        losses = losses_player_game[key] + 0

        if(losses == 0)
            ratio = "-"
        else
            ratio = sprintf("%.2f" , wins/losses)

        printf "%s,%s,%d,%d,%s\n",
                gamer,game,wins,losses,ratio 
        }
    
}
' history.csv | {
    read header
    echo "$header"

    if [ "$sort_by" = "wins" ]; then
    sort -t',' -k3,3nr
    elif [ "$sort_by" = "losses" ]; then
    sort -t',' -k4,4nr
    elif [ "$sort_by" = "ratio" ]; then
    sort -t',' -k5,5nr
    else
    sort -t',' -k3,3nr
    fi
    
} | column -t -s','


