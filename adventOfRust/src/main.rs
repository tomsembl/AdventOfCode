fn main() {
    let input = "1000
2000
3000

4000

5000
6000

7000
8000
9000

10000";
    let max = input.split("\n\n").map(|group|{
        group.lines().map(|line|{
            line.parse::<u32>().unwrap()
        }).sum::<u32>()
    }).max().unwrap();
    println!("{max:?}");
}