use std::{
    cell::RefCell,
    collections::{hash_map::Entry, HashMap, HashSet},
    fs::read_to_string,
    rc::Rc,
};

use lazy_static::lazy_static;
use regex::Regex;

lazy_static! {
    static ref RE: Regex = Regex::new(r"(?P<name>\w+ \w+) bags").unwrap();
    static ref RE2: Regex = Regex::new(r"(?P<n>\d+) (?P<name>\w+ \w+)").unwrap();
}

type BagPtr = Rc<RefCell<Bag>>;

#[derive(Debug)]
struct Bag {
    name: String,
    children: Vec<(BagPtr, usize)>,
    parents: Vec<BagPtr>,
}

fn get_or_insert<F>(map: &mut HashMap<String, BagPtr>, name: &str, f: F) -> BagPtr
where
    F: Fn(&str) -> BagPtr,
{
    match map.entry(name.to_owned()) {
        Entry::Occupied(e) => e.get().clone(),
        Entry::Vacant(_) => {
            let child = f(name);
            map.insert(name.to_owned(), child.clone());
            child
        }
    }
}

impl Bag {
    fn new_ptr(name: &str, children: Vec<(BagPtr, usize)>) -> BagPtr {
        Rc::new(RefCell::new(Bag {
            name: name.to_owned(),
            children,
            parents: Vec::new(),
        }))
    }
}

fn parse_file(path: &str) -> HashMap<String, BagPtr> {
    let mut map = HashMap::<String, BagPtr>::new();

    for line in read_to_string(path).unwrap().lines() {
        let mut split = line.split(" contain ");
        let name = RE
            .captures(split.next().unwrap())
            .unwrap()
            .name("name")
            .unwrap()
            .as_str();

        let parent = get_or_insert(&mut map, name, |n| Bag::new_ptr(n, Vec::new()));

        let children: Vec<(BagPtr, usize)> = split
            .next()
            .unwrap()
            .split(", ")
            .filter_map(|s| RE2.captures(s))
            .map(|s| {
                (
                    {
                        let child =
                            get_or_insert(&mut map, s.name("name").unwrap().as_str(), |name| {
                                Bag::new_ptr(name, Vec::new())
                            });
                        child.borrow_mut().parents.push(parent.clone());
                        child
                    },
                    s.name("n").unwrap().as_str().parse().unwrap(),
                )
            })
            .collect();

        parent.borrow_mut().children = children;
    }
    map
}

fn find_parents_rec(entry: &BagPtr, mut set: &mut HashSet<String>) {
    let b = entry.borrow();
    for parent in b.parents.iter() {
        set.insert(parent.borrow().name.clone());
        find_parents_rec(parent, &mut set);
    }
}

fn find_children_rec(entry: &BagPtr) -> usize {
    let b = entry.borrow();
    let mut ret = b.children.iter().map(|c| c.1).sum();
    for child in b.children.iter() {
        ret += child.1 * find_children_rec(&child.0);
    }

    ret
}

#[cfg(test)]
mod test {
    use std::collections::HashSet;

    use super::{find_children_rec, find_parents_rec, parse_file};

    #[test]
    fn d7p1() {
        let txt = parse_file("res/reddit/d7");
        let bag = txt.get("shiny gold").unwrap();
        let mut s = HashSet::new();
        find_parents_rec(bag, &mut s);
        println!("Solution: {}", s.len());
    }

    #[test]
    fn d7p2() {
        let txt = parse_file("res/reddit/d7");
        let bag = txt.get("shiny gold").unwrap();
        println!("Solution: {}", find_children_rec(bag));
    }
}
