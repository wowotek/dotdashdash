# DotDashDash
python implementation text-to-morse encoder or morse-to-text decoder using International Morse Code Standards

## Installing
1. Download the source code
   ```
   $ git clone https://github.com/wowotek/dotdashdash
   ```
2. move _`dotdashdash`_ library to your project directory
   ```
   $ mv ./dotdashdash your/project/directory
   ```

## Documentation
dotdashdash module provide easy encoding and decoding a plaintext and/or morse code to vice versa

dotdashdash module defines the following function :

1. _`dotdashdash`_**`.text_to_morse`**`(`_`text`_`)`:
   - _parameter_ : _`text`_ -> **`str`**
   - _return type_ : **`str`**
   - Encode _`text`_ to morse code
2. _`dotdashdash`_**`.morse_to_text`**`(`_`morse`_`)`:
   - _parameter_ : _`morse`_ -> **`str`**
   - _return type_ : **`str`**
   - Decode _`morse`_ to Plain text

## Usage
1. Import _`dotdashdash`_ library
   ```
   import dotdashdash as ddd
   ```
2. Use the library
    1. To Encode Text to Morse Code:
       ```
       ddd.text_to_morse("Hello World")
       ```
    2. To Decode Morse Code to Text:
       ```
       ddd.morse_to_text(".... . .-.. .-.. -.  .-- -. .-. .-.. -..")
       ```
   
