use std::fs;

const BOARD_SIZE: i64 = 5;

type NumberList = Vec<i64>;

#[derive(Debug)]
struct Board {
    board: NumberList,
    marked: NumberList,
}
type Boards = Vec<Board>;

impl Board {
    fn new(board: NumberList) -> Board {
        Board {
            board,
            // marked: vec![31, 27, 67, 13, 42],
            marked: vec![31, 23, 52, 26, 8],
        }
    }

    fn index(&self, i: i64, j: i64) -> usize {
        return (i * BOARD_SIZE + j) as usize;
    }

    fn print(&self) {
        for index in 0..self.board.len() {
            print!("{:>2} ", self.board[index]);
            if (index as i64 + 1) % BOARD_SIZE == 0 {
                print!("\n");
            };
        }
        println!();
    }

    fn get_val(&self, col: i64, row: i64) -> i64 {
        self.board[self.index(col, row)]
    }

    fn is_row_or_column(&self) -> bool {
        // Check rows first
        for row in 0..BOARD_SIZE {
            let start = row * BOARD_SIZE;
            let end = start + BOARD_SIZE;
            // This is wrong to check for columns.
            // All the marked numbers should be contained in the LHS comparison
            println!("{:?}", self.marked);
            for val in &self.board[start as usize..end as usize] {
                println!("{val}");
                if !self.marked.contains(val) {
                    return false;
                }
            }
        }

        // Check columns
        for col in 0..BOARD_SIZE {
            let index = 0;
            // let column = vec![self.board[]];
        }

        return true;
    }
}

fn parse_input(filename: &str) -> (NumberList, Boards) {
    let content =
        fs::read_to_string(filename).expect("Something went wrong when reading the file :/");
    let input = content.lines().collect::<Vec<&str>>();
    let number_lst: NumberList = input[0]
        .split(",")
        .into_iter()
        .map(|x| x.parse::<i64>().unwrap())
        .collect();

    let mut boards = vec![];
    let mut tmp_board = vec![];

    // Second line we know it's empty
    for raw_board in &input[2..] {
        if *raw_board == "" {
            let board = Board::new(tmp_board);
            println!("{}", board.is_row_or_column());
            boards.push(board);
            tmp_board = vec![];
            break;
            continue;
        };

        let mut parsed_board = raw_board
            .split_whitespace()
            .map(|x| x.parse::<i64>().unwrap())
            .collect::<Vec<i64>>();

        tmp_board.append(&mut parsed_board);
    }
    (number_lst, boards)
}

fn part1(filename: &str) {
    let (numbers, boards) = parse_input(filename);
}

fn main() {
    let filename = "src/day_4/input.txt";
    part1(filename);
}
