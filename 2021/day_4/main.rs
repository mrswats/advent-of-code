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
            marked: vec![],
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

    fn is_win(&self) -> bool {
        for pos in 0..BOARD_SIZE {
            let start = pos * BOARD_SIZE;
            let end = start + BOARD_SIZE;
            // This is wrong to check for columns.
            // All the marked numbers should be contained in the LHS comparison
            // Check rows first
            for val in &self.board[start as usize..end as usize] {
                if !self.marked.contains(val) {
                    return false;
                }
            }

            let mut col = Vec::<i64>::new();

            for val in 0..BOARD_SIZE {
                col.push(self.board[self.index(pos, val)])
            }

            for val in col {
                if !self.marked.contains(&val) {
                    return false;
                }
            }
        }

        return true;
    }

    fn result(&self, last_number_called: &i64) -> i64 {
        let mut sum = 0;
        for number in &self.board {
            if !self.marked.contains(&number) {
                sum += number;
            }
        }
        sum * last_number_called
    }
}

fn parse_input(filename: &str) -> (NumberList, Boards) {
    let content =
        fs::read_to_string(filename).expect("Something went wrong when reading the file :/");
    let input = content.lines().collect::<Vec<&str>>();
    let number_lst: NumberList = input[0]
        .split(",")
        .into_iter()
        .filter_map(|x| x.parse::<i64>().ok())
        .collect();

    let mut boards = vec![];
    let mut tmp_board = vec![];

    // Second line we know it's empty
    for raw_board in &input[2..] {
        if *raw_board == "" {
            continue;
        }

        let mut parsed_board = raw_board
            .split_whitespace()
            .filter_map(|x| x.parse::<i64>().ok())
            .collect::<Vec<i64>>();

        println!("{:?}", parsed_board);

        tmp_board.append(&mut parsed_board);

        if tmp_board.len() == 25 {
            let board = Board::new(tmp_board);
            boards.push(board);
            tmp_board = vec![];
        };
    }

    (number_lst, boards)
}

fn part1(filename: &str) {
    let (_numbers, _boards) = parse_input(filename);
}

fn main() {
    let filename = "src/day_4/test_input.txt";
    let filename = "src/day_4/input.txt";
    part1(filename);
}
