let open_input filename = 
  let channel = open_in filename in
  let rec get_lines acc =
    try 
      let line = input_line channel in
      get_lines (line :: acc)
    with e ->
      List.rev acc
  in get_lines []

let () =
  let lines = open_input "input.txt" in
  let rec sol l =
    match l with 
    | [] -> 0
    | hd::tl -> 
      match (String.split_on_char 'x' hd) with
      | l::w::h::[] -> 
                   let l = int_of_string l in 
                   let w = int_of_string w in 
                   let h = int_of_string h in
                   (l*w*h) + (let m = min ((l * 2) + (h * 2)) ((h * 2) + (w * 2)) in min m ((w * 2) + (l * 2))) + sol tl
      | _ -> 0
  
    in print_endline (string_of_int (sol lines))