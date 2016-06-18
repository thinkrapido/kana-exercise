#!/usr/bin/env python

import os, sys

from PIL import Image, ImageDraw, ImageFont
import numpy as np

def mkdir(dir):
  try:
      os.stat(dir)
  except:
      os.mkdir(dir)

syllables = [
  'a',    'i',   'u',  'e',  'o',
  'ka',  'ki',  'ku', 'ke', 'ko',
  'sa', 'shi',  'su', 'se', 'so',
  'ta', 'chi', 'tsu', 'te', 'to',
  'na',  'ni',  'nu', 'ne', 'no',
  'ha',  'hi',  'fu', 'he', 'ho',
  'ma',  'mi',  'mu', 'me', 'mo',
  'ya',   '.',  'yu',  '.', 'yo',
  'ra',  'ri',  'ru', 're', 'ro',
  'wa',   '.',   '.',  '.', 'w(o)',
  'n'
]

def generateSyllable():
  out = np.random.choice(syllables, 1)[0]
  if not out == '.': return out
  else: return generateSyllable()

class Syllable(object):

  size = 100

  def __init__(self, x, y, factor):
    self.x = x
    self.y = y
    self.factor = factor
    self.syllable = generateSyllable()

  def draw(self):
    global im

    draw = ImageDraw.Draw(im)

    boxWidth = self.size * self.factor

    font = ImageFont.truetype("arial.ttf", self.size)
    size = draw.textsize(self.syllable, font=font)
    width = np.max(size) * 1.3
    factor = boxWidth / width

    font = ImageFont.truetype("arial.ttf", (int) (boxWidth * factor * .8))
    size = draw.textsize(self.syllable, font=font)
    dX = (boxWidth - size[0]) / 2
    dY = (boxWidth - size[1]) / 2

    draw.text((self.x + dX, self.y + dY), self.syllable, fill='black', font=font)

    for i in range(4):
      draw.rectangle([(self.x, self.y + i * boxWidth),(self.x + boxWidth, self.y + boxWidth)], outline='black')


size = 3000
im = Image.new('RGB', ((int)(size * np.sqrt(2)), size), 'white')

offsetX = 30
offsetY = 100
width = 35
height = 7

for x in range(width):
  x = x * Syllable.size * 1.2 + offsetX
  for y in range(height):
    y = y * Syllable.size * 4 + offsetY

    s = Syllable(x,y,1)
    s.draw()






mkdir('out')
im.save('out/sheet1.png')


