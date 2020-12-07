#![allow(dead_code)]
use std::fs::read_to_string;

mod d1;
mod d2;
mod d3;
mod d4;
mod d5;
mod d6;
mod d7;
mod password;

fn main() {
    println!("Hello, world!");
}

fn _read_number_file(path: &str) -> Vec<i64> {
    read_to_string(path)
        .unwrap()
        .lines()
        .map(|line| line.parse::<i64>().unwrap())
        .collect()
}
