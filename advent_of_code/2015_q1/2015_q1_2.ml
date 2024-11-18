let explode s = List.init (String.length s) (String.get s)
let s = 
  let channel = open_in "input.txt" in
  let length = in_channel_length channel in
  let content = really_input_string channel length in
  close_in channel;
  content

let rec sol s acc idx = 
  if acc = -1 then 
    idx
  else
    match s with 
    | '('::tl -> sol tl (acc + 1) (idx + 1)
    | ')'::tl -> sol tl (acc - 1) (idx + 1)
    | _ -> 0

let () = 
  let res = sol (explode s) 0 0 in
  print_endline (string_of_int res);