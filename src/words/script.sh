declare -a words=( "bed"  "follow"  "rescue"  "passage"  "mix"  "aid"  "opera"  "observer"  "tease"  "banana"  "wound"  "cylinder"  "boat"  "friend"  "appetite"  "want"  "prevalence"  "product"  "owl"  "ice"  "stem"  "lemon"  "stress"  "egg"  "white"  "performer"  "attitude"  "protect"  "panic"  "sleep"  "desire")

index=0
for word in ${words[@]}
do
    echo $word > word_$index.txt
    index=$((index+1))
done
list="$(find ./ -maxdepth 1 -name "word_*.txt" | paste -sd " " | xargs -0)"
# eval "find ./ -maxdepth 1 -name "word_*.txt" zip {words.txt} +"
eval "zip words.zip $list"
 