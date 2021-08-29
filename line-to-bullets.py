import sys
import clipboard as clip

def main():
    # define bullet character
    bullet_character = input("Give bullet character(s) (default `-`): ")
    if len(bullet_character) == 0:
        bullet_character = "-"
    
    # ascertain space between bullet and list or no
    add_space = input("Do you want to add space between the bullet and text? " +
                      "(default `yes`, write `no` to say otherwise) ")
    if add_space.upper() == "NO":
        add_space = False
    else:
        add_space = True
    
    # after directions, read all lines passed in
    print("Give input to print out.",
          "Press [key] to see them be rewritten.")
    print("[key] if from IDLE (or Unix-like) is Enter then Ctrl+D.\n" +
          "[key] if from cmd is Enter, Ctrl+Z, then Enter")
    print("NOTE: [IDLE only] if copy/pasting lines of data with a " +
          "terminating line break, " +
          "you will need to remove the extra line break.\n" +
          "Follow the directions afterward.")
    msg = sys.stdin.readlines()
    
    # add formatting to lines
    for idx in range(len(msg)):
        msg[idx] = '{}{}{}'.format(bullet_character, " " if add_space else '',
                                   msg[idx].strip('\n'))
    
    # print out for the user
    for line in msg:
        print(line)
    
    # copy to clipboard
    clip.copy('\n'.join(str(line) for line in msg))
    
    # verify completion
    print("Bullet addition completed; check your clipboard")
    
main()
