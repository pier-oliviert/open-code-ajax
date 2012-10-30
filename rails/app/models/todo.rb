class Todo < ActiveRecord::Base
  attr_accessible :done, :title

  validates :title, :length => { :minimum => 3 }
end
